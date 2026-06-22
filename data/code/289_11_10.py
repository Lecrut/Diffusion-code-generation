def validate_meters(meters):
    if not all(isinstance(m, (int, float)) for m in meters):
        raise ValueError("All elements must be numbers.")

def convert_meters_to_feet(meters):
    validate_meters(meters)
    return [round(m * 3.28084, 2) for m in meters]

if __name__ == '__main__':
    sample_meters = [10.0, 20.0, 30.0]
    converted_feet = convert_meters_to_feet(sample_meters)
    print(f"Converted feet: {converted_feet}")