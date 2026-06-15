def create_animal_sentiment_store():
    animal_data = {
        "lion": 8,
        "tiger": 9,
        "elephant": 7,
        "monkey": 5,
        "penguin": 3,
        "snake": 2
    }
    return animal_data
if __name__ == '__main__':
    animal_favorites = create_animal_sentiment_store()
    print(animal_favorites)