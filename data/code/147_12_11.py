def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Input must be a list of dictionaries")

def sort_dicts_by_key(data, key):
    validate_input(data)
    return sorted(data, key=lambda x: x.get(key, float('-inf')), reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    print("Original data:", sample_data)
    sorted_data = sort_dicts_by_key(sample_data, 'age')
    print("Sorted by age (descending):", sorted_data)