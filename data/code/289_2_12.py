def inches_to_millimeters(inches):
    if not isinstance(inches, (int, float)):
        raise ValueError('Input must be a number.')
    return inches * 25.4
if __name__ == '__main__':
    print(inches_to_millimeters(1))