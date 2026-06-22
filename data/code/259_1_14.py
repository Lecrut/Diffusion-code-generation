def find_min_max(data):
    min_val = float('inf')
    max_val = float('-inf')
    for num in data:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_min_max(sample_values)
    print(result)