UNIT_CONVERSION = {'feet': 12, 'yards': 36, 'miles': 63360}

def feet_to_inches(feet_value: float) -> float:
    return feet_value * UNIT_CONVERSION['feet']

if __name__ == '__main__':
    input_feet = 10
    output_inches = feet_to_inches(input_feet)
    print(output_inches)