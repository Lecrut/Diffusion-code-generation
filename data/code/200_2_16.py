def validate_float_list(float_list):
    if not all(isinstance(num, (int, float)) for num in float_list):
        raise ValueError("All elements in the list must be floats.")

def sum_positive_values(float_list):
    total = 0
    for value in float_list:
        if value > 0:
            total += value
    return total

if __name__ == '__main__':
    sample_values = [1.5, -2.3, 4.8, 0.0, -1.1, 3.2]
    validate_float_list(sample_values)
    result = sum_positive_values(sample_values)
    print(result)