def convert_feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a number")
    if feet < 0:
        raise ValueError("Input must be non-negative")
    return feet * 12

if __name__ == '__main__':
    sample_feet = 5
    result = convert_feet_to_inches(sample_feet)
    print(result)
    sample_feet = 2.5
    result = convert_feet_to_inches(sample_feet)
    print(result)