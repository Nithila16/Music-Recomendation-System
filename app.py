from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#app
app = Flask(__name__)


#load save data
df = pd.read_csv("clustered_df.csv")


def recommend_songs(song_name, df, num_recommendations=5):
    # Get the cluster of the input song
    song_cluster = df[df["name"] == song_name]["Cluster"].values[0]
    same_cluster_songs = df[df["Cluster"] == song_cluster]
    song_index = same_cluster_songs[same_cluster_songs["name"] == song_name].index[0]
    cluster_features = same_cluster_songs[numerical_features]
    similarity = cosine_similarity(cluster_features, cluster_features)
    similar_songs = np.argsort(similarity[song_index])[-(num_recommendations + 1):-1][::-1]
    recommendations = same_cluster_songs.iloc[similar_songs][["name", "year", "artists"]]
    return recommendations

#route
@app.route('/')
def index():
    return render_template('index.html')

#API END POINT
@app.route("/recommend",methods=['GET','POST'])
def recommend():
    recommendations = []
    
    if request.method == "POST":
        song_name = request.form.get("song_name")


        try:
            # Assuming recommend_songs takes a string and returns a DataFrame
            recommendations_df = recommend_songs(song_name_df)
            if recommendations_df is None or recommendations_df.empty:
                raise ValueError("No recommendations found")
            recommendations = recommendations_df.to_dict(orient="records")

        except Exception as e:
            print(f"Error: {e}")  # Logging the error for debugging
           
    
    return render_template("index.html", recommendations=recommendations)


#python app call
if __name__ == '__main__':
    app.run(debug=True)