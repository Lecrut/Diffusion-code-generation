INCHES_PER_FOOT = 12

def _multiply_by_constant(value, factor):
    return value * factor

def feet_to_inches(feet):
    return _multiply_by_constant(feet, INCHES_PER_FOOT)

if __name__ == '__main__':
    input_feet = 14
    conversion_result = feet_to_inches(input_feet)
    print(conversion_result)