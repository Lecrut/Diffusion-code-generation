def convert_feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Feet must be a number")
    return feet * 12

if __name__ == '__main__':
    inches_result = convert_feet_to_inches(5)
    print(inches_result)