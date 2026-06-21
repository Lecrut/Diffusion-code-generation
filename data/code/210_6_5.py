def compute_range(data):
    min_val = max_val = next(data)
    for val in data:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
    return (min_val, max_val)

if __name__ == '__main__':
    sample_data = (i * i for i in range(1000000))
    print(compute_range(sample_data))