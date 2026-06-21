def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

if __name__ == '__main__':
    sample_gallons = 5
    converted_liters = gallons_to_liters(sample_gallons)
    print(converted_liters)