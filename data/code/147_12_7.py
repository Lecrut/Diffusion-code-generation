def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x.get(key, float('-inf')), reverse=True)

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie'},
        {'name': 'David', 'age': 35}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'age')
    print(sorted_dicts)