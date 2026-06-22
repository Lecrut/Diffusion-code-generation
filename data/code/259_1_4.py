def find_min_max(data):
    min_val = data[0]
    max_val = data[0]
    for num in data:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [7, 3, 9, 1, 5, 2, 8, 6, 4]
    result = find_min_max(sample_values)
    print(result)