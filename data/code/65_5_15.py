UNIT_CONVERSIONS = {'feet_to_inches': 12}

def calculate_inches_from_feet(feet):
    return feet * UNIT_CONVERSIONS['feet_to_inches']

if __name__ == '__main__':
    inches = calculate_inches_from_feet(5)
    print(inches)