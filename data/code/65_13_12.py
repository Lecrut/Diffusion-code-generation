def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a numeric type (int or float)")
    return int(feet * 12) if feet == int(feet) else feet * 12

if __name__ == '__main__':
    sample_feet = 5.5
    result = feet_to_inches(sample_feet)
    print(result)