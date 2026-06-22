conversion_factors = {
    'cubic_meters_to_gallons': 264.172
}

def cubic_meters_to_gallons(cubic_meters):
    return cubic_meters * conversion_factors['cubic_meters_to_gallons']

if __name__ == '__main__':
    print(cubic_meters_to_gallons(1))
    print(cubic_meters_to_gallons(2))