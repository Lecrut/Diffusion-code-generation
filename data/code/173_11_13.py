from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'product': 'laptop', 'price': 1200},
        {'product': 'phone', 'price': 800},
        {'product': 'laptop', 'price': 1300},
        {'product': 'tablet', 'price': 600}
    ]
    grouped_by_product = group_by_key(sample_data, 'product')
    print(grouped_by_product)