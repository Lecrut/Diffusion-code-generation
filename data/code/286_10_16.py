def inches_to_cm(inches):
    conversion_factor = 2.54
    return inches * conversion_factor

if __name__ == '__main__':
    sample_inches = 15
    centimeters = inches_to_cm(sample_inches)
    print(f"{sample_inches} inches is equal to {centimeters:.2f} centimeters")