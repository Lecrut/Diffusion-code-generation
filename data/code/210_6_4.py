def compute_range(data):
    min_val = max_val = next(data)
    for value in data:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return max_val - min_val

if __name__ == '__main__':
    sample_data = (i**2 for i in range(1000000))
    print(compute_range(sample_data))