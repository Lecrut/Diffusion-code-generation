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
    if 'apples' not in data:
        data['apples'] = 0
    if 'bananas' not in data:
        data['bananas'] = 0
    if 'oranges' not in data:
        data['oranges'] = 0
    data['apples'] = data.get('apples', 0) + 5
    data['bananas'] = data.get('bananas', 0) - 2
    data['oranges'] = data.get('oranges', 0) + 10
    save_data(data)
    return data
if __name__ == '__main__':
    print("--- Initial State ---")
    initial_data = load_data()
    print(initial_data)
    print("\n--- After Management Operation ---")
    final_data = manage_item_counts()
    print(final_data)
    print("\n--- Final State Saved to File ---")
    final_loaded_data = load_data()
    print(final_loaded_data)