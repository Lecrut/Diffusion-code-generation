def extract_maximum(data_points):
    if not data_points:
        raise ValueError("Cannot extract maximum from empty sequence")
    if not all(isinstance(x, float) for x in data_points):
        raise TypeError("All elements must be floats")
    return max(data_points)

if __name__ == '__main__':
    sample_data = (1.5, 3.7, 2.1, 9.3, 4.8)
    result = extract_maximum(sample_data)
    print(result)