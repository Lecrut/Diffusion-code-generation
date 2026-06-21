def sort_objects_by_key(objects, key):
    return sorted(objects, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'item': 'Apple', 'quantity': 10},
        {'item': 'Banana', 'quantity': 5},
        {'item': 'Cherry', 'quantity': 7}
    ]
    sorted_data = sort_objects_by_key(sample_data, 'quantity')
    print(sorted_data)