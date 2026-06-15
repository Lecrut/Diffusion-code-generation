def track_favorite_animals():
    favorite_animals = {
        "Dog": ["Playful", "Loyal"],
        "Cat": ["Independent", "Graceful"],
        "Elephant": ["Wise", "Gentle"],
        "Lion": ["Brave", "Regal"]
    }
    return favorite_animals
if __name__ == '__main__':
    animal_data = track_favorite_animals()
    print(animal_data)