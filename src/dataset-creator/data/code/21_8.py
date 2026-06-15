import itertools
def organize_data(data):
    result = {}
    for item in data:
        key = (item['name'], item['id'])
        result[key] = item
    return result
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'id': 101, 'value': 10},
        {'name': 'Bob', 'id': 102, 'value': 20},
        {'name': 'Alice', 'id': 101, 'value': 15},
        {'name': 'Charlie', 'id': 103, 'value': 30},
        {'name': 'Bob', 'id': 102, 'value': 25}
    ]
    organized_dict = organize_data(sample_data)
    print(organized_dict)