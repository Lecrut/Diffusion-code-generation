CONVERSION_FACTOR = 1 / 2.54

def convert_cm_to_inches(cm):
    if not isinstance(cm, (int, float)):
        raise ValueError("Input must be a number.")
    return cm * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_cm = 50
    inches = convert_cm_to_inches(sample_cm)
    print(inches)