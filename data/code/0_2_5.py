def inches_to_centimeters(inches):
    return inches * 2.54

if __name__ == '__main__':
    sample_inches = [0, 1, 5, 12, 100]
    for inches in sample_inches:
        cm = inches_to_centimeters(inches)
        print(f"{inches} inches = {cm} centimeters")