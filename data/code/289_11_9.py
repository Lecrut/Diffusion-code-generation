def meters_to_feet(meters):
    return [round(meter * 3.28084, 2) for meter in meters]

if __name__ == '__main__':
    sample_meters = [10, 20, 30]
    converted_feet = meters_to_feet(sample_meters)
    print(f"Converted feet: {converted_feet}")