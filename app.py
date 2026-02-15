import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Movie Recommender", page_icon="🎬")

# Load movie data
data = pd.read_csv("movies.csv")

st.title("🎬 Smart Movie Recommendation System")

st.write("Select your preferred genre and minimum rating to get suggestions.")

# Unique genres
genres = data["genre"].unique()

selected_genre = st.selectbox("Choose Genre", genres)
min_rating = st.slider("Minimum Rating", 5.0, 10.0, 7.0)

# Filtering logic
filtered_movies = data[
    (data["genre"] == selected_genre) &
    (data["rating"] >= min_rating)
]

if st.button("Get Recommendations"):
    if filtered_movies.empty:
        st.warning("No movies found for selected criteria.")
    else:
        st.success(f"Found {len(filtered_movies)} movies!")
        for index, row in filtered_movies.iterrows():
            st.subheader(row["title"])
            st.write(f"⭐ Rating: {row['rating']}")
            st.write(row["description"])
            st.markdown("---")