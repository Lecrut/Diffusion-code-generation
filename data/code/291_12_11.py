def validate_feet_inches(feet, inches):
    if not (isinstance(feet, (int, float)) and isinstance(inches, (int, float))):
        raise ValueError('Feet and inches must be numbers')
    if not (feet >= 0 and inches >= 0):
        raise ValueError('Feet and inches must be non-negative')
    if not inches < 12:
        raise ValueError('Inches must be less than 12')

def convert_to_inches(feet, inches):
    return feet * 12 + inches

def compare_feet_inches(feet1, inches1, feet2, inches2):
    validate_feet_inches(feet1, inches1)
    validate_feet_inches(feet2, inches2)
    total_inches1 = convert_to_inches(feet1, inches1)
    total_inches2 = convert_to_inches(feet2, inches2)
    if total_inches1 > total_inches2:
        return ((feet1, inches1), 'feet')
    elif total_inches2 > total_inches1:
        return ((feet2, inches2), 'feet')
    else:
        return ((feet1, inches1), 'inches')
if __name__ == '__main__':
    result = compare_feet_inches(5.5, 3, 6, 0)
    print(result)