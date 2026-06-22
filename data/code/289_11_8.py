def convert_meters_to_feet(meters):
    if not all(isinstance(meter, (int, float)) for meter in meters):
        raise ValueError("All input values must be numbers.")
    return [round(meter * 3.28084, 2) for meter in meters]

if __name__ == '__main__':
    sample_meters = [10, 20, 30]
    converted_feet = convert_meters_to_feet(sample_meters)
    print(f"Converted feet: {converted_feet}")