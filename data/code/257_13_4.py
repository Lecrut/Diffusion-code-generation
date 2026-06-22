def calculate_value_difference(data):
    if not isinstance(data, dict) or not all(isinstance(v, int) for v in data.values()):
        raise ValueError("Input must be a dictionary with integer values")
    if len(data) == 0:
        return 0
    return max(data.values()) - min(data.values())

if __name__ == '__main__':
    sample_data = {
        'a': 10,
        'b': 20,
        'c': 5,
        'd': 30
    }
    print(calculate_value_difference(sample_data))