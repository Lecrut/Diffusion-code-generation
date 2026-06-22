CONVERSION_FACTOR = 4 / 5

def celsius_to_reaumur(celsius):
    return celsius * CONVERSION_FACTOR

if __name__ == '__main__':
    print(celsius_to_reaumur(0))
    print(celsius_to_reaumur(100))
    print(celsius_to_reaumur(-40))