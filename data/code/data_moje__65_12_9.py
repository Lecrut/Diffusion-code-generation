CONVERSION_RATIO = 12.0

def feet_to_inches(feet):
    return feet * CONVERSION_RATIO

if __name__ == '__main__':
    feet_value = 5
    inches_value = feet_to_inches(feet_value)
    print(inches_value)