def track_animal_favorites():
    favorites = {}
    animal1 = "dog"
    preferences1 = ["friendly", "loyal"]
    favorites[animal1] = preferences1
    animal2 = "cat"
    preferences2 = ["affectionate", "independent"]
    favorites[animal2] = preferences2
    animal3 = "lion"
    preferences3 = ["majestic", "fierce"]
    favorites[animal3] = preferences3
    animal4 = "elephant"
    preferences4 = ["large", "intelligent"]
    favorites[animal4] = preferences4
    return favorites
if __name__ == '__main__':
    animal_data = track_animal_favorites()
    print(animal_data)