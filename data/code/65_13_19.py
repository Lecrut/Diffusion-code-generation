def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a numeric type (int or float)")
    return feet * 12

if __name__ == '__main__':
    sample_values = [1, 2.5, 0, -3, 100]
    for value in sample_values:
        result = feet_to_inches(value)
        print(result)