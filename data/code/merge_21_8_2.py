import itertools
def organize_data(data):
    result = {}
    for item in data:
        key = (item['name'], item['id'])
        result[key] = item
    return result
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'id': 101, 'value': 50},
        {'name': 'Bob', 'id': 102, 'value': 75},
        {'name': 'Alice', 'id': 101, 'value': 55},
        {'name': 'Charlie', 'id': 103, 'value': 90},
        {'name': 'Bob', 'id': 102, 'value': 80}
    ]
    organized_dict = organize_data(sample_data)
    print(organized_dict)