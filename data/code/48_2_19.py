def extract_max_float(data_points: tuple) -> float:
    if not data_points:
        raise ValueError("Sequence is empty")
    if not all(isinstance(x, (int, float)) for x in data_points):
        raise TypeError("All elements must be numeric")
    return max(float(x) for x in data_points)

if __name__ == '__main__':
    sample_data = (3.14, 2.71, 1.41, 9.81, 0.57)
    result = extract_max_float(sample_data)
    print(result)