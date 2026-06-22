def inches_to_centimeters(inches):
    conversion_factor = 2.54
    return inches * conversion_factor
if __name__ == '__main__':
    sample_inches = 10
    result = inches_to_centimeters(sample_inches)
    print(result)