from collections import defaultdict

def group_by_key(data_list, key):
    grouped_data = defaultdict(list)
    for item in data_list:
        if key in item:
            category = item[key]
            grouped_data[category].append(item)
    return dict(grouped_data)

if __name__ == '__main__':
    sample_data = [
        {'product': 'Laptop', 'price': 1200, 'brand': 'Dell'},
        {'product': 'Smartphone', 'price': 800, 'brand': 'Samsung'},
        {'product': 'Tablet', 'price': 350, 'brand': 'Apple'},
        {'product': 'Laptop', 'price': 1400, 'brand': 'HP'}
    ]
    grouping_key = 'brand'
    
    grouped_products = group_by_key(sample_data, grouping_key)
    print(grouped_products)