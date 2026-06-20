CONVERSION_FACTOR = 2.54

def inches_to_centimeters(value):
    input_value = float(value)
    calculated_result = input_value * CONVERSION_FACTOR
    return calculated_result

if __name__ == '__main__':
    test_length = 42.75
    output_cm = inches_to_centimeters(test_length)
    print(output_cm)