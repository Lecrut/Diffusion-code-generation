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
    print("Initial Data Loaded:", data)
    data['apples'] = 10
    data['bananas'] = 5
    data['oranges'] = 15
    print("Data after modification:", data)
    save_data(data)
if __name__ == '__main__':
    manage_item_counts()