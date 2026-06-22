CONVERSION_FACTOR = 5280.0

def miles_to_feet(miles):
    if miles < 0:
        raise ValueError("Miles must be positive")
    return miles * CONVERSION_FACTOR

if __name__ == '__main__':
    print(miles_to_feet(1.0))
    print(miles_to_feet(3.7))
    print(miles_to_feet(0.25))