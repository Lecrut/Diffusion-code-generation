INCHES_PER_FOOT = 12

def feet_to_inches(feet):
    if feet < 0:
        raise ValueError("Feet cannot be negative")
    if not isinstance(feet, (int, float)):
        raise TypeError("Feet must be a number")
    return feet * INCHES_PER_FOOT

if __name__ == '__main__':
    sample_feet = 10.5
    computed_inches = feet_to_inches(sample_feet)
    print(computed_inches)