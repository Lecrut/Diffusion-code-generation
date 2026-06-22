def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("Input must be a number")
    if feet < 0:
        raise ValueError("Feet cannot be negative")
    return feet * 12

if __name__ == '__main__':
    print(feet_to_inches(1))
    print(feet_to_inches(5.5))
    print(feet_to_inches(0))