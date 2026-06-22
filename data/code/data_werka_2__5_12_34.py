METERS_TO_CENTIMETERS = 100

def convert_and_compare(meters1, meters2):
    cm1 = meters1 * METERS_TO_CENTIMETERS
    cm2 = meters2 * METERS_TO_CENTIMETERS
    return meters1 if cm1 > cm2 else meters2

if __name__ == '__main__':
    value1 = 6.0
    value2 = 4.5
    larger_value = convert_and_compare(value1, value2)
    print(larger_value)