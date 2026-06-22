def print_values(data, key):
    for item in data:
        if key in item:
            print(item[key])

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    print_values(sample_data, 'name')