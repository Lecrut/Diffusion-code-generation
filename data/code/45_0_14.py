def find_minimum(values):
    if not values:
        raise ValueError("List must not be empty")
    return min(values)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_minimum(sample_values)
    print(result)