def sort_objects_by_key(objects, key):
    return sorted(objects, key=lambda obj: obj.get(key, None))

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_data = sort_objects_by_key(sample_data, 'age')
    print(sorted_data)