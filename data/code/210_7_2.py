def calculate_range(data):
    if not data:
        return None
    min_val = data[0]
    max_val = data[0]
    for x in data:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return (min_val, max_val)
if __name__ == '__main__':
    sample_data = [10, 3.5, -5, 22.1, 0]
    result = calculate_range(sample_data)
    print(result)