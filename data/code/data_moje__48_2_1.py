def extract_max_float(data: tuple) -> float:
    if not data:
        raise ValueError("Cannot extract maximum from an empty sequence")
    max_val = max(data)
    if not isinstance(max_val, float):
        raise TypeError("Sequence must contain only float values")
    return max_val

if __name__ == '__main__':
    sample_data = (1.5, 3.7, 2.2, 4.1)
    result = extract_max_float(sample_data)
    print(result)