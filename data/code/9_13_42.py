def gallons_to_liters(gallons):
    liters_per_gallon = 3.78541
    return gallons * liters_per_gallon

if __name__ == '__main__':
    sample_gallons = 5
    converted_liters = gallons_to_liters(sample_gallons)
    print(converted_liters)