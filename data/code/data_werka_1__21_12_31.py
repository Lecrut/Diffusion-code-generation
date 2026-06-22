def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'product': 'Laptop', 'price': 1200},
        {'product': 'Smartphone', 'price': 800},
        {'product': 'Tablet', 'price': 450}
    ]
    sorted_data = sort_dicts_by_key(sample_data, 'price')
    print(sorted_data)