def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a numeric type (int or float)")
    if isinstance(feet, bool):
        raise TypeError("Input must be a numeric type (int or float)")
    return feet * 12

if __name__ == '__main__':
    sample_values = [0, 1, 5.5, 10, -3.2]
    for value in sample_values:
        result = feet_to_inches(value)
        print(result)