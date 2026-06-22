FEET_TO_INCHES = 12

def convert_feet_to_inches(feet):
    return feet * FEET_TO_INCHES

if __name__ == '__main__':
    feet_value = 10
    result = convert_feet_to_inches(feet_value)
    print(result)