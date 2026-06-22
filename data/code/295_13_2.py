conversion_factors = {
    'gallons_to_liters': 3.78541,
    'liters_to_gallons': 0.264172
}

def gallons_to_liters(gallons):
    return gallons * conversion_factors['gallons_to_liters']

def liters_to_gallons(liters):
    return liters * conversion_factors['liters_to_gallons']

if __name__ == '__main__':
    print(gallons_to_liters(1))
    print(liters_to_gallons(1))