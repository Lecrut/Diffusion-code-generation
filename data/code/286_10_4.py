conversion_factors = {
    'inches_to_cm': 2.54,
}

def inches_to_cm(inches):
    return inches * conversion_factors['inches_to_cm']

if __name__ == '__main__':
    sample_inches = [1, 10, 100]
    for inches in sample_inches:
        cm = inches_to_cm(inches)
        print(f"{inches} inches is equal to {cm:.2f} centimeters")