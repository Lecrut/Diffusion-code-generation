from collections import defaultdict
def organize_data(data, sort_key):
    organized = defaultdict(list)
    for item in data:
        if sort_key in item:
            key_value = item[sort_key]
            organized[key_value].append(item)
    return dict(organized)
if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 30, 'city': 'New York'},
        {'name': 'David', 'age': 35, 'city': 'Chicago'},
        {'name': 'Eve', 'age': 25, 'city': 'Los Angeles'}
    ]
    sort_key_1 = 'city'
    result_1 = organize_data(sample_data, sort_key_1)
    print(f"Organized by '{sort_key_1}':")
    print(result_1)
    sort_key_2 = 'age'
    result_2 = organize_data(sample_data, sort_key_2)
    print(f"\nOrganized by '{sort_key_2}':")
    print(result_2)
    sort_key_3 = 'name'
    result_3 = organize_data(sample_data, sort_key_3)
    print(f"\nOrganized by '{sort_key_3}':")
    print(result_3)