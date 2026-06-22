def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a numeric type")
    if isinstance(feet, bool):
        raise TypeError("Input must be a numeric type")
    if isinstance(feet, complex):
        raise TypeError("Input must be a real numeric type")
    return int(feet) * 12 if feet == int(feet) else feet * 12

if __name__ == '__main__':
    sample_values = [5, 5.5, 0, -2]
    for val in sample_values:
        print(feet_to_inches(val))