def gallons_to_liters(gallons):
    conversion_factor = 3.78541
    liters = gallons * conversion_factor
    return liters

if __name__ == '__main__':
    sample_gallons = 5
    result = gallons_to_liters(sample_gallons)
    print(result)