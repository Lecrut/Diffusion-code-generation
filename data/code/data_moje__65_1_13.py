INCHES_PER_FOOT = 12

def convert_feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

if __name__ == '__main__':
    feet = 10
    inches = convert_feet_to_inches(feet)
    print(inches)