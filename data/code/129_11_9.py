def validate_data(data):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in data):
        raise ValueError("Data must be a list of tuples with two elements each.")

def sort_by_criteria(data):
    validate_data(data)
    return sorted(data, key=lambda x: (-x[0], x[1]))

if __name__ == '__main__':
    sample_data = [
        (3, 'Banana'),
        (2, 'Apple'),
        (3, 'Cherry'),
        (2, 'Date'),
        (3, 'Avocado'),
        (1, 'Carrot'),
    ]
    sorted_data = sort_by_criteria(sample_data)
    for item in sorted_data:
        print(item)