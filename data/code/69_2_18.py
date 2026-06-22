CONVERSION_FACTOR = 5280
miles_to_feet = lambda miles: 0 if miles <= 0 else miles * CONVERSION_FACTOR
if __name__ == '__main__':
    print(miles_to_feet(-5))
    print(miles_to_feet(0))
    print(miles_to_feet(3.5))