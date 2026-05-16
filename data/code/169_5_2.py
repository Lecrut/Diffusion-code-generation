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
    print("Initial data loaded.")
    apples = data['apples']
    bananas = data['bananas']
    oranges = data['oranges']
    print(f"Current counts: Apples={apples}, Bananas={bananas}, Oranges={oranges}")
    apples += 5
    bananas -= 2
    oranges += 10
    save_data(data)
    print("Data updated and saved.")
    final_data = load_data()
    print(f"Final counts loaded from file: Apples={final_data.get('apples')}, Bananas={final_data.get('bananas')}, Oranges={final_data.get('oranges')}")
if __name__ == '__main__':
    manage_item_counts()