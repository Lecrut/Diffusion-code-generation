def find_smallest_value(values):
    if not values:
        return None
    smallest = float('inf')
    for value in values:
        if isinstance(value, float) and value < smallest:
            smallest = value
    return smallest

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 0.577, -1.618, 1.414]
    print(find_smallest_value(sample_values))