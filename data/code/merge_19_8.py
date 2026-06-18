import json
data_file = "favorite_animals.json"
def load_data():
    try:
        with open(data_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
def save_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f)
def add_animal(animals, new_name):
    animals.append(new_name)
    save_data(animals)
def view_animals(animals):
    if not animals:
        print("No favorite animals are currently tracked.")
        return
    print("--- Favorite Animals ---")
    for i, animal in enumerate(animals):
        print(f"{i+1}. {animal}")
if __name__ == '__main__':
    data = load_data()
    sample_names = ["Lion", "Tiger", "Elephant", "Bear"]
    print("--- Adding Sample Favorite Animals ---")
    for name in sample_names:
        add_animal(data, name)
        print(f"Added: {name}")
    print("\n--- Viewing All Tracked Animals ---")
    view_animals(data)