import json
data_file = "objects.json"
sample_data = [
    {"id": 1, "name": "Apple", "category": "Fruit", "details": "Red and sweet"},
    {"id": 2, "name": "Carrot", "category": "Vegetable", "details": "Orange root"},
    {"id": 3, "name": "Banana", "category": "Fruit", "details": "Yellow and soft"},
    {"id": 4, "name": "Broccoli", "category": "Vegetable", "details": "Green and leafy"}
]
with open(data_file, 'w') as f:
    json.dump(sample_data, f)
def organize_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    organized_dict = {}
    for item in data:
        category = item.get('category', 'Unknown')
        if category not in organized_dict:
            organized_dict[category] = []
        organized_dict[category].append(item)
    return organized_dict
if __name__ == '__main__':
    result = organize_data(data_file)
    print(json.dumps(result, indent=4))