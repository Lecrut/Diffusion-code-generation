def inches_to_cm(inches):
    conversion_factor = 2.54
    return inches * conversion_factor

if __name__ == '__main__':
    sample_inches = [1, 10, 100]
    for inches in sample_inches:
        cm = inches_to_cm(inches)
        print(f"{inches} inches is equal to {cm} centimeters")