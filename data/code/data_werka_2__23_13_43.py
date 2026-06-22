def compare_values(value1, value2):
    try:
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise ValueError("Both values must be either integers or floats.")
        
        if value1 > value2:
            return "First value is greater than the second value."
        elif value1 < value2:
            return "First value is less than the second value."
        else:
            return "First value is equal to the second value."
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    sample_value1 = 3.14
    sample_value2 = 2.71
    result = compare_values(sample_value1, sample_value2)
    print(result)