conversion_factor = 2.54

def calculate_cm_from_inches(inches):
    return inches * conversion_factor

if __name__ == '__main__':
    sample_inches = 12
    cm_value = calculate_cm_from_inches(sample_inches)
    print(f"{sample_inches} inches is {cm_value} cm")