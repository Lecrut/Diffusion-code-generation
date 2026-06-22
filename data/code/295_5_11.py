conversion_factor = 2.54

def calculate_conversion(inches):
    return inches * conversion_factor

if __name__ == '__main__':
    sample_inches = 15
    cm_value = calculate_conversion(sample_inches)
    print(f"{sample_inches} inches is {cm_value} cm")