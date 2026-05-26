from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
#data ={
     
movi_names=[
      "movie_names",
        "marvel",
        "avengers",
        "bateman",
        "superhero",
        "titanic",
        "notebook",




    ],
tags=[
         "super hero marvel fight",
         "dark hero hero action dc",
         "super hero flying action",
         "romance ship love emotional",
         "romance love emotional drama",
         "super hero action sex",


]


count =CountVectorizer()
matrix=count.fit_transform(tags)
cosine =cosine_similarity(matrix)
print("similar movies:",cosine)
movie =input("Enter your name:")
vector =count. transform([movie])
cosi =cosine_similarity(vector,matrix)
print(f"result according to your movie name:{cosi}")


