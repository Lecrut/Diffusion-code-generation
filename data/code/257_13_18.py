def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if not all(isinstance(v, int) for v in data.values()):
        raise ValueError("Dictionary values must be integers")

def calculate_value_difference(data):
    validate_input(data)
    return max(data.values()) - min(data.values())

if __name__ == '__main__':
    sample_data = {
        'a': 10,
        'b': 20,
        'c': 5,
        'd': 30
    }
    print(calculate_value_difference(sample_data))