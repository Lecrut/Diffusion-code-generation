def find_max_optimized(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for i in range(1, len(data)):
        if data[i] > max_val:
            max_val = data[i]
    return max_val
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, 9.999, -1.0, 5.0]
    try:
        maximum = find_max_optimized(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)