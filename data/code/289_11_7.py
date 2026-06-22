conversion_factor = {'meters': 3.28084}

def convert_meters_to_feet(meters):
    feet = meters * conversion_factor['meters']
    return round(feet, 2)

if __name__ == '__main__':
    sample_meters = [10.0, 25.0, 50.0]
    converted_feet = [convert_meters_to_feet(m) for m in sample_meters]
    print(converted_feet)