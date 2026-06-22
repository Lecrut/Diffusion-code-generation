conversion_factor = {
    'meters': 3.28084
}

def meters_to_feet(meters):
    return [round(meter * conversion_factor['meters'], 2) for meter in meters]

if __name__ == '__main__':
    sample_meters = [10, 20, 30]
    result_feet = meters_to_feet(sample_meters)
    print(result_feet)