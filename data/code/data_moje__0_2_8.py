def inches_to_centimeters(inches):
    return inches * 2.54

if __name__ == '__main__':
    sample_inches = [1, 12, 36, 0.5, 100]
    for inches in sample_inches:
        result = inches_to_centimeters(inches)
        print(result)