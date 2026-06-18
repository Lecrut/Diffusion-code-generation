def create_animal_sentiment_store():
    animal_data = {
        "lion": 8,
        "tiger": 9,
        "elephant": 7,
        "monkey": 6,
        "penguin": 5,
        "snake": 3
    }
    return animal_data
if __name__ == '__main__':
    sentiment_store = create_animal_sentiment_store()
    print(sentiment_store)