import json
FILE_NAME = "item_counts.json"
def load_data():
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
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
        data = initial_data
        save_data(data)
        print("Data initialized and saved.")
    print("--- Initial Data Loaded ---")
    print(data)
    print("\n--- Modifying Data ---")
    data["apple"] += 3
    data["banana"] -= 1
    data["grape"] = 20
    print("Data after modification:")
    print(data)
    save_data(data)
    print("\nData saved successfully to", FILE_NAME)
if __name__ == '__main__':
    manage_item_counts()