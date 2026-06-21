def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x[key])

if __name__ == '__main__':
    sample_data = [
        {'item': 'apple', 'price': 1.2},
        {'item': 'banana', 'price': 0.8},
        {'item': 'cherry', 'price': 3.5}
    ]
    sorted_data = sort_dicts_by_key(sample_data, 'price')
    print(sorted_data)