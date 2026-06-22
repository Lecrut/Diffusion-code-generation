CONVERSION_MAP = {
    "feet_to_inches": 12
}

def convert_length(value, unit_type):
    ratio = CONVERSION_MAP[unit_type]
    return value * ratio

if __name__ == '__main__':
    input_feet = 7
    output_inches = convert_length(input_feet, "feet_to_inches")
    print(output_inches)