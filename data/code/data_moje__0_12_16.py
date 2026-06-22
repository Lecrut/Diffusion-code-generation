CENTIMETERS_TO_INCHES_RATIO = 1 / 2.54
PRECISION_MULTIPLIER = 10000

def calculate_inches(length_cm: float) -> float:
    intermediate_value = length_cm * CENTIMETERS_TO_INCHES_RATIO
    scaled_value = intermediate_value * PRECISION_MULTIPLIER
    rounded_value = round(scaled_value)
    return rounded_value / PRECISION_MULTIPLIER

if __name__ == '__main__':
    test_length = 75
    output = calculate_inches(test_length)
    print(output)