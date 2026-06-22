CONVERSION_FACTOR = 5280

def miles_to_feet(miles):
    total_feet = miles * CONVERSION_FACTOR
    return float(total_feet)

if __name__ == '__main__':
    test_distance = 3.75
    feet_result = miles_to_feet(test_distance)
    print(feet_result)