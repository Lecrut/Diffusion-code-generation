FOOT_TO_INCH_RATIO = 12

def convert_feet_to_inches(feet):
    return feet * FOOT_TO_INCH_RATIO

if __name__ == '__main__':
    feet_value = 5
    inches = convert_feet_to_inches(feet_value)
    print(inches)