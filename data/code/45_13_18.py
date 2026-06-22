def find_minimum(values):
    if not values:
        return None
    min_val = values[0]
    for num in values:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [34, -50, 42, 14, -10, 75, 0]
    result = find_minimum(sample_list)
    print(result)