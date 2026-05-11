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
if __name__ == '__main__':
    item_counts = load_data()
    if not item_counts:
        item_counts = {
            "apple": 10,
            "banana": 5,
            "orange": 12
        }
    print("Initial counts:", item_counts)
    item_counts["apple"] += 3
    item_counts["banana"] -= 1
    item_counts["grape"] = 20
    save_data(item_counts)
    print("Updated counts:", item_counts)
    new_item_counts = load_data()
    print("Data loaded after modification:", new_item_counts)