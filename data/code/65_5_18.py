def validate_input(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number")
    return value

def feet_to_inches(feet):
    validated = validate_input(feet)
    return validated * 12

if __name__ == '__main__':
    inches = feet_to_inches(5)
    print(inches)