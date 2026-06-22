CONVERSION_FACTOR = 25.4

def inches_to_millimeters(inches):
    if not isinstance(inches, (int, float)):
        raise ValueError("Invalid input. Use an integer or float for inches.")
    return inches * CONVERSION_FACTOR

if __name__ == '__main__':
    result = inches_to_millimeters(1)
    print(result)