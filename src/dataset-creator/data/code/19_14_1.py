def display_favorite_animals(animal_list):
    print("--- Favorite Animals ---")
    for animal in animal_list:
        print(f"- {animal}")
    print("------------------------")
if __name__ == '__main__':
    favorite_animals = [
        "Dog",
        "Cat",
        "Elephant",
        "Lion",
        "Whale"
    ]
    display_favorite_animals(favorite_animals)