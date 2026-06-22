def inches_to_centimeters(inches):
    conversion_factor = 2.54
    centimeters = inches * conversion_factor
    return centimeters

if __name__ == '__main__':
    sample_inches = 10
    result_cm = inches_to_centimeters(sample_inches)
    print(result_cm)