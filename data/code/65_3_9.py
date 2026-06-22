CONVERSION_FACTOR_INCHES_PER_FOOT = 12

def feet_to_inches(feet):
    if feet < 0:
        return -feet * CONVERSION_FACTOR_INCHES_PER_FOOT
    return feet * CONVERSION_FACTOR_INCHES_PER_FOOT

if __name__ == '__main__':
    test_value = 12.0
    output = feet_to_inches(test_value)
    print(output)