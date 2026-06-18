def create_animal_sentiment_store():
    animal_data = {
        "lion": 8,
        "elephant": 7,
        "monkey": 5,
        "tiger": 9,
        "penguin": 4,
        "giraffe": 6
    }
    return animal_data
if __name__ == '__main__':
    animal_favorites = create_animal_sentiment_store()
    print(animal_favorites)