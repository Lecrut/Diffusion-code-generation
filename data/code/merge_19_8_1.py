import json
data_file = "favorites.json"
def load_favorites():
    try:
        with open(data_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
def save_favorites(favorites):
    with open(data_file, 'w') as f:
        json.dump(favorites, f)
def add_animal(favorites, new_name):
    favorites.append(new_name)
    save_favorites(favorites)
def view_animals(favorites):
    if not favorites:
        print("No animals are currently tracked.")
        return
    print("--- Tracked Animals ---")
    for i, animal in enumerate(favorites):
        print(f"{i + 1}. {animal}")
if __name__ == '__main__':
    favorites = load_favorites()
    sample_animals = ["Lion", "Tiger", "Elephant", "Bear"]
    print("--- Adding Sample Animals ---")
    for animal in sample_animals:
        add_animal(favorites, animal)
        print(f"Added: {animal}")
    print("\n--- Viewing All Tracked Animals ---")
    view_animals(favorites)