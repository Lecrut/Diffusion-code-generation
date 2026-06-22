FEET_TO_INCHES_FACTOR = 12

def convert_feet_to_inches(feet):
    return feet * FEET_TO_INCHES_FACTOR

if __name__ == '__main__':
    result = convert_feet_to_inches(10)
    print(result)