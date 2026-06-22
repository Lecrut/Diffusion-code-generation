def validate_gallons(gallons):
    if not isinstance(gallons, (int, float)):
        raise ValueError("Volume must be a number")
    if gallons < 0:
        raise ValueError("Gallons cannot be negative")

def convert_gallons_to_liters(gallons):
    liters_per_gallon = 3.78541
    validate_gallons(gallons)
    return gallons * liters_per_gallon

if __name__ == '__main__':
    sample_volume_gallons = 6.0
    try:
        converted_liters = convert_gallons_to_liters(sample_volume_gallons)
        print(converted_liters)
    except ValueError as e:
        print(e)