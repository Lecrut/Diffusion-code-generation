def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    SAMPLE_KEY = 'salary'
    sample_dicts = [
        {'employee': 'Alice', 'salary': 70000},
        {'employee': 'Bob', 'salary': 85000},
        {'employee': 'Charlie', 'salary': 60000}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, SAMPLE_KEY)
    print(sorted_dicts)