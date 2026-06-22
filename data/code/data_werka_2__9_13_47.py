def gallons_to_liters(gallons):
    liters_per_gallon = 3.78541
    return gallons * liters_per_gallon

if __name__ == '__main__':
    sample_volume_gallons = 20.0
    conversion_result = gallons_to_liters(sample_volume_gallons)
    print(conversion_result)