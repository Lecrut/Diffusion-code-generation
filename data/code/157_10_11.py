def find_smallest_value(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_values = [34, 12, 56, 9, 88, 23, 10]
    result = find_smallest_value(sample_values)
    print(result)