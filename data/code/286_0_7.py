CONVERSION_FACTOR = 2.54

def inches_to_centimeters(inches):
    return inches * CONVERSION_FACTOR

if __name__ == '__main__':
    print(inches_to_centimeters(1))
    print(inches_to_centimeters(10))
    print(inches_to_centimeters(100))