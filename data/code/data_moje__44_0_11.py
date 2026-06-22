def validate_numeric_sequence(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if not data:
        raise ValueError("Input list cannot be empty")
    for index, value in enumerate(data):
        if not isinstance(value, int):
            raise TypeError(f"Element at index {index} is not an integer")
    return data

def compute_mean(values):
    validated_values = validate_numeric_sequence(values)
    total_sum = 0
    element_count = len(validated_values)
    for number in validated_values:
        total_sum += number
    return total_sum / element_count

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    output = compute_mean(sample_data)
    print(output)