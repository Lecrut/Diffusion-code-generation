def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Eve', 'score': 85},
        {'name': 'Dan', 'score': 92},
        {'name': 'Frank', 'score': 78}
    ]
    sort_key = 'score'
    sorted_data = sort_dicts_by_key(sample_data, sort_key)
    print(sorted_data)