def filter_and_sort(data, condition_key, condition_value, sort_key):
    filtered_data = [item for item in data if item.get(condition_key) == condition_value]
    sorted_filtered_data = sorted(filtered_data, key=lambda x: x[sort_key])
    return sorted_filtered_data

if __name__ == '__main__':
    sample_data = [
        {'product': 'Laptop', 'price': 1200},
        {'product': 'Smartphone', 'price': 800},
        {'product': 'Tablet', 'price': 450},
        {'product': 'Smartphone', 'price': 900},
        {'product': 'Headphones', 'price': 150}
    ]
    result = filter_and_sort(sample_data, 'product', 'Smartphone', 'price')
    for item in result:
        print(item)