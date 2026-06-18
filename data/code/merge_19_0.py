def track_favorite_animals():
    favorite_animals = {
        "Lion": ["majestic", "kingly"],
        "Elephant": ["wise", "gentle"],
        "Tiger": ["fierce", "striped"],
        " Dolphin": ["intelligent", "playful"]
    }
    return favorite_animals
if __name__ == '__main__':
    animal_data = track_favorite_animals()
    print(animal_data)