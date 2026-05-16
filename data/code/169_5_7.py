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
if __name__ == '__main__':
    item_counts = load_data()
    item_counts['apple'] = 10
    item_counts['banana'] = 5
    item_counts['orange'] = 12
    save_data(item_counts)
    print(json.dumps(item_counts, indent=4))