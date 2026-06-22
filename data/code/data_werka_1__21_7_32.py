def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda d: d.get(key))

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    
    sorted_data = sort_dicts_by_key(sample_data, 'age')
    print(sorted_data)