def sort_objects_by_key(objects, key):
    return sorted(objects, key=lambda x: x.get(key))
if __name__ == '__main__':
    sample_data = [{'product': 'Laptop', 'price': 1200}, {'product': 'Smartphone', 'price': 800}, {'product': 'Tablet', 'price': 450}]
    sorted_data = sort_objects_by_key(sample_data, 'price')
    print(sorted_data)