def validate_length(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Length must be a number.")

def convert_to_meters(length_feet):
    validate_length(length_feet)
    return length_feet * 0.3048

if __name__ == '__main__':
    length_feet = 10.0
    result_meters = convert_to_meters(length_feet)
    print(f"10.0 ft converted to meters: {result_meters}")