def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
        raise ValueError("Input must be a list of integers")

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    validate_input(sample_values)
    largest_value = max(sample_values)
    print(largest_value)