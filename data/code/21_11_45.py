def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'product': 'Apple', 'price': 1.2},
        {'product': 'Banana', 'price': 0.5},
        {'product': 'Cherry', 'price': 2.0}
    ]
    sort_key = 'price'
    sorted_products = sort_dicts_by_key(sample_data, sort_key)
    print(sorted_products)