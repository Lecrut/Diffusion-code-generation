conversion_factors = {
    'inches_to_cm': 2.54,
    'cm_to_inches': 1 / 2.54
}

def inches_to_cm(inches):
    return inches * conversion_factors['inches_to_cm']

def cm_to_inches(cm):
    return cm * conversion_factors['cm_to_inches']

if __name__ == '__main__':
    print(f"Inches to Centimeters:")
    print(inches_to_cm(1))
    print(inches_to_cm(0.5))
    print("\nCentimeters to Inches:")
    print(cm_to_inches(2.54))
    print(cm_to_inches(12.7))