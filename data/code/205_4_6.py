from operator import itemgetter

def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Input must be a list of dictionaries.")

def sort_dicts_by_key(dicts, key):
    validate_input(dicts)
    return sorted(dicts, key=itemgetter(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'age')
    print(sorted_dicts)