def find_minimum(values):
    if not values:
        raise ValueError("List cannot be empty")
    min_val = values[0]
    for num in values[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [15, 3, 89, 42, 7, 102, 3, 55, 12]
    result = find_minimum(sample_data)
    print(result)