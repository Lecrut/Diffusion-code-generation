def validate_feet_inches(feet, inches):
    if not (isinstance(feet, (int, float)) and isinstance(inches, (int, float))):
        raise ValueError("Feet and inches must be numbers.")
    if feet < 0 or inches < 0:
        raise ValueError("Feet and inches cannot be negative.")
    if inches >= 12:
        raise ValueError("Inches must be less than 12.")

def convert_to_inches(feet, inches):
    return feet * 12 + inches

def compare_lengths(length1_feet, length1_inches, length2_feet, length2_inches):
    validate_feet_inches(length1_feet, length1_inches)
    validate_feet_inches(length2_feet, length2_inches)
    
    total_inches1 = convert_to_inches(length1_feet, length1_inches)
    total_inches2 = convert_to_inches(length2_feet, length2_inches)
    
    if total_inches1 > total_inches2:
        return (length1_feet, length1_inches, "feet")
    elif total_inches2 > total_inches1:
        return (length2_feet, length2_inches, "feet")
    else:
        rounded_inches = round(total_inches1 / 12) * 12
        return (rounded_inches // 12, rounded_inches % 12, "inches")

if __name__ == '__main__':
    print(compare_lengths(5, 3.5, 4, 11))
    print(compare_lengths(3, 8, 3, 7))
    print(compare_lengths(2, 0, 2, 0))