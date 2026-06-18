import sys
animals = ["Lion", "Tiger", "Elephant"]
def add_animal(new_animal):
    animals.append(new_animal)
def view_animals():
    for animal in animals:
        print(animal)
if __name__ == '__main__':
    print("--- Favorite Animals ---")
    print("Currently tracked animals:")
    view_animals()
    print("\n--- Adding New Favorites (Sample Data) ---")
    add_animal("Bear")
    add_animal("Wolf")
    print("\n--- Updated List of Favorite Animals ---")
    view_animals()