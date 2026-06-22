def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a numeric type (int or float)")
    return feet * 12

if __name__ == '__main__':
    print(feet_to_inches(5))
    print(feet_to_inches(3.5))
    print(feet_to_inches(0))
    print(feet_to_inches(-2.5))