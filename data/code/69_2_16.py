CONVERSION_FACTORS = {'miles_to_feet': 5280}

miles_to_feet = lambda miles: miles * CONVERSION_FACTORS['miles_to_feet']

if __name__ == '__main__':
    print(miles_to_feet(1))
    print(miles_to_feet(2.5))
    print(miles_to_feet(10))