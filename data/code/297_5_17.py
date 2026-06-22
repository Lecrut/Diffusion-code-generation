def inches_to_centimeters(inches):
    if not isinstance(inches, (int, float)):
        raise ValueError('Input must be a number')
    return inches * 2.54
if __name__ == '__main__':
    print(inches_to_centimeters(1))
    print(inches_to_centimeters(0))
    try:
        print(inches_to_centimeters('a'))
    except ValueError as e:
        print(e)