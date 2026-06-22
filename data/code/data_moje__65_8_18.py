UNIT_INCHES_PER_FOOT = 12

def convert_feet_to_inches(value_in_feet: float) -> float:
    return value_in_feet * UNIT_INCHES_PER_FOOT

if __name__ == '__main__':
    input_feet = 12
    output_inches = convert_feet_to_inches(input_feet)
    assert output_inches == 144
    print(output_inches)