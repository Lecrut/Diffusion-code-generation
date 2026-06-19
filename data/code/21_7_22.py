def sort_objects_by_key(objects, key):
    return sorted(objects, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    
    sorted_data = sort_objects_by_key(sample_data, 'age')
    print(sorted_data)