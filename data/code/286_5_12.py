def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be a number.")
    return value

def nanometers_to_meters(nanometers):
    meters = validate_input(nanometers) * 1e-9
    return meters

if __name__ == '__main__':
    sample_nanos = 1000000000
    converted_meters = nanometers_to_meters(sample_nanos)
    print(f"{sample_nanos} nanometers is equal to {converted_meters} meters")