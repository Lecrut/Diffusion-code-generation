def filter_items(data, key, value):
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Data must be a list of dictionaries")
    if not isinstance(key, str):
        raise ValueError("Key must be a string")
    
    filtered = [item for item in data if item.get(key) == value]
    return sorted(filtered, key=lambda x: x['score'], reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'item': 'Apple', 'score': 85},
        {'item': 'Banana', 'score': 92},
        {'item': 'Cherry', 'score': 78},
        {'item': 'Date', 'score': 92},
        {'item': 'Elderberry', 'score': 88}
    ]
    result = filter_items(sample_data, 'item', 'Banana')
    print(result)