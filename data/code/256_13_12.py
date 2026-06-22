def validate_data(data):
    if not data:
        raise ValueError("Data cannot be empty")
    for value in data:
        if not isinstance(value, (int, float)):
            raise TypeError("All elements must be numbers")

def calculate_range(data):
    min_val = float('inf')
    max_val = float('-inf')
    for value in data:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return max_val - min_val

if __name__ == '__main__':
    sample_data = [10, 25, 35, 45, 60]
    validate_data(sample_data)
    print(calculate_range(sample_data))