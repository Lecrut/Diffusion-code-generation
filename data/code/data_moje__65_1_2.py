FEET_TO_INCHES = 12

def feet_to_inches(feet):
    return feet * FEET_TO_INCHES

if __name__ == '__main__':
    feet_value = 10
    inches_value = feet_to_inches(feet_value)
    print(inches_value)