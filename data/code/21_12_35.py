def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 92},
        {'name': 'Charlie', 'score': 78}
    ]
    sort_key = 'score'
    sorted_data = sort_dicts_by_key(sample_data, sort_key)
    print(sorted_data)