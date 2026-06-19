def sort_objects_by_key(objects, key):
    return sorted(objects, key=lambda obj: obj.get(key))

if __name__ == '__main__':
    sample_objects = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    
    sorted_objects = sort_objects_by_key(sample_objects, 'age')
    print(sorted_objects)