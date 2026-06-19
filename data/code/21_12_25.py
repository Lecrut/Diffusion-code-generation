def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x.get(key, 0), reverse=True)

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35}
    ]
    
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'age')
    print(sorted_dicts)