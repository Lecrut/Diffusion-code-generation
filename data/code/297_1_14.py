GALLON_TO_LITER = 3.78541

def convert_gallons_to_liters(gallons):
    return gallons * GALLON_TO_LITER

if __name__ == '__main__':
    sample_gallons = 5
    result = convert_gallons_to_liters(sample_gallons)
    print(result)