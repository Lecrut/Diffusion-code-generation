def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return round(centimeters, 1)

if __name__ == '__main__':
    sample_inches = 36.0
    result = inches_to_centimeters(sample_inches)
    print(result)