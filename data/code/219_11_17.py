def find_max_efficiently(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for value in data[1:]:
        if value > max_val:
            max_val = value
    return max_val

if __name__ == '__main__':
    sample_list = [3.14159, 2.71828, -0.5, 10.0, 99.99999999999999]
    try:
        maximum = find_max_efficiently(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)