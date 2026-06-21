def validate_values(value1, value2):
    if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
        raise ValueError("Both values must be either integers or floats.")

def compare_values(value1, value2):
    validate_values(value1, value2)
    
    if value1 > value2:
        return "First value is greater than the second value."
    elif value1 < value2:
        return "First value is less than the second value."
    else:
        return "First value is equal to the second value."

if __name__ == '__main__':
    sample_value1 = 50
    sample_value2 = 30
    result = compare_values(sample_value1, sample_value2)
    print(result)