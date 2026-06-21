def find_maximum(data):
    if not isinstance(data, list) or not all(isinstance(x, float) for x in data):
        raise ValueError("Input must be a list of floats")
    if not data:
        raise ValueError("Data list is empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10.5, 4.2, 25.7, 8.3, 30.1]
    maximum = find_maximum(sample_list)
    print(maximum)