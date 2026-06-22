def find_minimum(data):
    min_val = None
    for item in data:
        if min_val is None or item < min_val:
            min_val = item
    return min_val

if __name__ == '__main__':
    sample_data = [3, -1, 4, 1, -5, 9, 2, -6]
    result = find_minimum(sample_data)
    print(result)