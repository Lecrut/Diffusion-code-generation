def inches_to_centimeters(inches):
    return inches * 2.54

if __name__ == '__main__':
    sample_inch_values = [0, 1, 12, 36.5, 100]
    for val in sample_inch_values:
        print(inches_to_centimeters(val))