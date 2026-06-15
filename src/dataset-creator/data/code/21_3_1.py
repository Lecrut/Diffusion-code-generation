def index_objects(data):
    result = {}
    for obj in data:
        identifier = obj.get('id')
        if identifier is not None:
            result[identifier] = obj
    return result
if __name__ == '__main__':
    sample_data = [
        {'id': 'A101', 'name': 'Alice', 'age': 30},
        {'id': 'B202', 'name': 'Bob', 'age': 25},
        {'id': 'C303', 'name': 'Charlie', 'age': 35},
        {'id': 'A101', 'name': 'Alice Duplicate', 'age': 31}
    ]
    indexed_data = index_objects(sample_data)
    print(indexed_data)