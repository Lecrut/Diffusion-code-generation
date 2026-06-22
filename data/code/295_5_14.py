conversion_factor = 2.54

def validate_inches(inches):
    if inches < 0:
        raise ValueError("Inches value must be non-negative")

def inches_to_cm(inches):
    validate_inches(inches)
    return inches * conversion_factor

if __name__ == '__main__':
    sample_inches = 10
    cm_value = inches_to_cm(sample_inches)
    print(f"{sample_inches} inches is {cm_value} cm")