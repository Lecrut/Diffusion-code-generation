def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a numeric type")
    return feet * 12

if __name__ == '__main__':
    sample_values = [0, 1, 5.5, -3, 100]
    for value in sample_values:
        result = feet_to_inches(value)
        print(result)