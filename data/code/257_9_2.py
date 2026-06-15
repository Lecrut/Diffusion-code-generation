def find_range(data):
    if not data:
        return None
    min_val = data[0]
    max_val = data[0]
    for x in data[1:]:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return max_val - min_val
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.999, -10.0, 5.0]
    result = find_range(sample_list)
    print(result)