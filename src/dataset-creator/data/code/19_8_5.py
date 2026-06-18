import sys
animals = ["Lion", "Tiger", "Elephant"]
def add_animal(new_animal):
    animals.append(new_animal)
def view_animals():
    for animal in animals:
        print(f"Tracked Animal: {animal}")
if __name__ == '__main__':
    print("--- Initializing Favorite Animal Tracker ---")
    print("Sample animals loaded:")
    view_animals()
    print("\n--- Adding New Sample Animals ---")
    add_animal("Bear")
    add_animal("Wolf")
    print("\n--- Viewing All Tracked Animals ---")
    view_animals()