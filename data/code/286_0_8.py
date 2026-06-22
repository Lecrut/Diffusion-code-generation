CONVERSION_FACTOR = 2.54

def inches_to_cm(inches):
    return inches * CONVERSION_FACTOR

if __name__ == '__main__':
    print(inches_to_cm(1))
    print(inches_to_cm(10))
    print(inches_to_cm(20))