def compute_range(data):
    min_val = max_val = next(data)
    for value in data:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return max_val - min_val

if __name__ == '__main__':
    sample_data = (x * x for x in range(1000000))
    result = compute_range(sample_data)
    print(result)