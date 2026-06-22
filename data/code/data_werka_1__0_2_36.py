def inches_to_centimeters(inches):
    return inches * 2.54

if __name__ == '__main__':
    sample_inch_values = [1, 6, 10, 20]
    for inch in sample_inch_values:
        cm = inches_to_centimeters(inch)
        print(f"{inch} inches is {cm} centimeters")