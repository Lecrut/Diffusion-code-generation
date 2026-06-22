CONVERSION_FACTOR = 2.54

def inches_to_centimeters(inches):
    return round(inches * CONVERSION_FACTOR, 1)
if __name__ == '__main__':
    print(inches_to_centimeters(1))
    print(inches_to_centimeters(5))
    print(inches_to_centimeters(10))
    print(inches_to_centimeters(3.5))
    print(inches_to_centimeters(0.5))