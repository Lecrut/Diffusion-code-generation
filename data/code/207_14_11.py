def find_maximum(data):
    if not isinstance(data, list) or not all(isinstance(item, float) for item in data):
        raise ValueError("Input must be a list of floats")
    if not data:
        raise ValueError("Data list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10.5, 5.2, 20.7, 8.3, 15.9]
    maximum_value = find_maximum(sample_list)
    print(maximum_value)