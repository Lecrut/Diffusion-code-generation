def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    min_val = data[0]
    max_val = data[0]
    for x in data:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return min_val, max_val
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    minimum, maximum = find_min_max(sample_list)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")