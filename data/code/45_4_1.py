def find_minimum(values):
    if not values:
        return None
    min_val = values[0]
    for x in values:
        if x < min_val:
            min_val = x
    return min_val

if __name__ == '__main__':
    sample_data = [34, -12, 56, 0, 99, -5, 1024, 42, 88, -100]
    result = find_minimum(sample_data)
    print(result)