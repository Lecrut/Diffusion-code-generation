def meters_to_feet(meters):
    if not isinstance(meters, list) or not all(isinstance(x, (int, float)) for x in meters):
        raise ValueError("Input must be a list of numbers.")
    
    return [round(meter * 3.28084, 2) for meter in meters]

if __name__ == '__main__':
    sample_meters = [10.0, 15.5, 20.0]
    try:
        result_feet = meters_to_feet(sample_meters)
        print(f"Meters: {sample_meters}, Converted to Feet: {result_feet}")
    except ValueError as e:
        print(e)