def track_favorite_animals():
    favorite_animals = {}
    animal1 = "cat"
    preferences1 = ["fluffy", "sleepy"]
    favorite_animals[animal1] = preferences1
    animal2 = "dog"
    preferences2 = ["playful", "loyal"]
    favorite_animals[animal2] = preferences2
    animal3 = "lion"
    preferences3 = ["majestic", "roar"]
    favorite_animals[animal3] = preferences3
    animal4 = "elephant"
    preferences4 = ["large", "grey"]
    favorite_animals[animal4] = preferences4
    return favorite_animals
if __name__ == '__main__':
    data = track_favorite_animals()
    print(data)