def find_min_with_loop(data):
    if not data:
        raise ValueError("Cannot find minimum of an empty list")
    min_val = data[0]
    for item in data:
        if item < min_val:
            min_val = item
    return min_val

if __name__ == '__main__':
    sample_list = [5, 3, 8, 1, 9, 2]
    result = find_min_with_loop(sample_list)
    print(result)