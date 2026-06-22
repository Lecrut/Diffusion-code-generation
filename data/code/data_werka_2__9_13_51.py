def convert_volume(gallons):
    conversion_table = {
        'gallons_to_liters': 3.78541
    }
    liters_per_gallon = conversion_table['gallons_to_liters']
    return gallons * liters_per_gallon

if __name__ == '__main__':
    sample_volume_gallons = 8.0
    converted_liters = convert_volume(sample_volume_gallons)
    print(converted_liters)