def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_value = data[0]
    for i in range(1, len(data)):
        if data[i] > max_value:
            max_value = data[i]
    return max_value
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.999, -1.0, 42.0]
    try:
        maximum = find_maximum(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)