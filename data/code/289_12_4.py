def inches_to_centimeters(inches):
    return round(inches * 2.54, 1)

if __name__ == '__main__':
    print(inches_to_centimeters(1))
    print(inches_to_centimeters(2.5))
    print(inches_to_centimeters(0))