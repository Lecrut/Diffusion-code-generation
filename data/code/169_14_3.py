import json
import os
DATA_FILE = "item_counts.json"
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)
def add_item(data, item, count):
    if item in data:
        data[item] += count
    else:
        data[item] = count
    save_data(data)
def view_counts(data):
    for item, count in data.items():
        print(f"{item}: {count}")
if __name__ == '__main__':
    data = load_data()
    print("--- Item Count Manager (Sample Run) ---")
    print("\nAction 1: Adding items (Sample Data)")
    add_item(data, "apples", 10)
    add_item(data, "bananas", 5)
    add_item(data, "apples", 3)
    print("\nAction 2: Viewing current counts")
    view_counts(data)
    print("\n--- Final State ---")
    view_counts(data)
    print("\nExiting program.")