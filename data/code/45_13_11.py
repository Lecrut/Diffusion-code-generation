def find_min_with_early_termination(values):
    if not values:
        return None
    min_val = values[0]
    for num in values:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [10, -5, 3, 7, -20, 4, 0]
    result = find_min_with_early_termination(sample_data)
    print(result)