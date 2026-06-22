UNIT_FACTORS = {
    "inch": 2.54,
    "ft": 30.48,
    "yd": 91.44
}

def inches_to_centimeters(value):
    factor = UNIT_FACTORS.get("inch")
    return value * factor

def format_result(input_val, converted_val):
    return f"{input_val} inches is {converted_val} cm"

if __name__ == '__main__':
    test_cases = [5, 10.5, 0, 100]
    for tc in test_cases:
        output = inches_to_centimeters(tc)
        print(format_result(tc, output))