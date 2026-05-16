import json
import os
DATA_FILE = "item_counts.json"
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}
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
    print("\n--- Adding Sample Items ---")
    add_item(data, "apples", 10)
    add_item(data, "bananas", 5)
    add_item(data, "oranges", 12)
    print("\n--- Viewing Current Counts ---")
    view_counts(data)
    print("\n--- Adding More Sample Items ---")
    add_item(data, "apples", 3)
    add_item(data, "grapes", 8)
    print("\n--- Final Counts ---")
    view_counts(data)
    print("\nProgram finished. Data saved to item_counts.json")