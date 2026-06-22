def gallons_to_liters(gallons):
    conversion_factor = 3.78541
    return gallons * conversion_factor

if __name__ == '__main__':
    sample_gallons = 5
    print(gallons_to_liters(sample_gallons))