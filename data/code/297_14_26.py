def validate_input(value):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError("Input must be a non-negative number")

def inches_to_cm(inches):
    validate_input(inches)
    return inches * 2.54

def cm_to_inches(cm):
    validate_input(cm)
    return cm / 2.54

if __name__ == '__main__':
    print(f"Inches to Centimeters:")
    print(inches_to_cm(1))
    print(inches_to_cm(0.5))
    print("\nCentimeters to Inches:")
    print(cm_to_inches(2.54))
    print(cm_to_inches(12.7))