def find_smallest_value(values):
    if not values:
        return None
    smallest = float('inf')
    for value in values:
        if isinstance(value, (int, float)) and value < smallest:
            smallest = value
    return smallest

if __name__ == '__main__':
    sample_values = [3.14, 2.71, -1.0, 0.0, 5.0]
    print(find_smallest_value(sample_values))