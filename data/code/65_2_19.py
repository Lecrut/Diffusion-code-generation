FEET_TO_INCHES_FACTOR = 12

def feet_to_inches(feet):
    if not isinstance(feet, (int, float)):
        raise TypeError("feet must be a number")
    return feet * FEET_TO_INCHES_FACTOR

if __name__ == '__main__':
    sample_feet = 10.5
    print(feet_to_inches(sample_feet))