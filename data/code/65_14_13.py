FEET_TO_INCHES_FACTOR = 12

def feet_to_inches(feet):
    return feet * FEET_TO_INCHES_FACTOR

if __name__ == '__main__':
    print(feet_to_inches(3))
    print(feet_to_inches(7.5))
    print(feet_to_inches(0))