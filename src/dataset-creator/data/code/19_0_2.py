def track_favorite_animals():
    favorite_animals = {
        "Dog": ["Playful", "Loyal"],
        "Cat": ["Independent", "Graceful"],
        "Lion": ["Majestic", "Strong"],
        "Elephant": ["Wise", "Gentle"]
    }
    return favorite_animals
if __name__ == '__main__':
    animal_data = track_favorite_animals()
    print(animal_data)