def find_smallest_value(data):
    smallest = float('inf')
    for value in data:
        if value < smallest:
            smallest = value
    return smallest

if __name__ == '__main__':
    sample_data = (10, 5, 2, 8, 1)
    result = find_smallest_value(sample_data)
    print(result)