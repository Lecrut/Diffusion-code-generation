CONVERSION_FACTOR = 2.54

def inches_to_cm(inches):
    return inches * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_inches = [1, 10, 100]
    for inch in sample_inches:
        cm = inches_to_cm(inch)
        print(f"{inch} inches is equal to {cm:.2f} centimeters")