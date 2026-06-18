import json
data_file = "animals.json"
def load_animals():
    try:
        with open(data_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
def save_animals(animals):
    with open(data_file, 'w') as f:
        json.dump(animals, f)
def add_animal(animals, new_name):
    animals.append(new_name)
    save_animals(animals)
def view_animals(animals):
    if not animals:
        print("No animals currently tracked.")
        return
    print("\n--- Tracked Animals ---")
    for i, animal in enumerate(animals):
        print(f"{i+1}. {animal}")
    print("----------------------")
if __name__ == '__main__':
    animals = load_animals()
    sample_names = ["Lion", "Tiger", "Elephant", "Bear"]
    print("--- Adding Sample Favorite Animals ---")
    for name in sample_names:
        add_animal(animals, name)
        print(f"Added: {name}")
    view_animals(animals)