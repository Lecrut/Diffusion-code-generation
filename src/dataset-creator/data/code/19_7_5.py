def create_animal_sentiment_store():
    animal_data = {
        "lion": 8,
        "elephant": 9,
        "tiger": 7,
        "monkey": 6,
        "penguin": 5,
        "giraffe": 8
    }
    return animal_data
if __name__ == '__main__':
    animal_favorites = create_animal_sentiment_store()
    print(animal_favorites)