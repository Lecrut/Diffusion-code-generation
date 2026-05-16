import json
import os
FILE_NAME = "item_counts.json"
def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, 'r') as f:
        return json.load(f)
def save_data(data):
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f)
def manage_item_counts():
    data = load_data()
    initial_data = {
        "apple": 10,
        "banana": 5,
        "orange": 12
    }
    if not data:
        data.update(initial_data)
    else:
        for key in initial_data:
            if key not in data:
                data[key] = initial_data[key]
            else:
                data[key] = initial_data[key]
    print("Initial Data Loaded/Set:")
    print(data)
    data["apple"] += 3
    data["banana"] -= 1
    data["grape"] = 20
    print("\nData after modifications:")
    print(data)
    save_data(data)
    print(f"\nData saved to {FILE_NAME}")
if __name__ == '__main__':
    manage_item_counts()