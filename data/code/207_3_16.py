def find_maximum(data):
    if not data or not isinstance(data, dict) or not all(isinstance(v, (int, float)) for v in data.values()):
        raise ValueError("Input must be a non-empty dictionary with numeric values.")
    return max(data.values(), key=float)

if __name__ == '__main__':
    sample_data = {
        'a': 15,
        'b': 8,
        'c': 22,
        'd': 4,
        'e': 30,
        'f': 11
    }
    result = find_maximum(sample_data)
    print(result)