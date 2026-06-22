def feet_to_inches(feet):
    if isinstance(feet, (int, float)):
        return feet * 12
    raise TypeError("Input must be a number")

if __name__ == '__main__':
    print(feet_to_inches(5))
    print(feet_to_inches(1.5))
    print(feet_to_inches(0))
    print(feet_to_inches(-3))