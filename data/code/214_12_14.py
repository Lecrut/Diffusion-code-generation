def find_smallest_value(values):
    if not values:
        raise ValueError("Input iterable is empty")
    return min(values)

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, -2.1, 0.0]
    print(find_smallest_value(sample_values))