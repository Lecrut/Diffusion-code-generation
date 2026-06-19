def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

if __name__ == '__main__':
    sample_meters = 5
    sample_feet = 10
    sample_kilograms = 15
    sample_pounds = 30
    sample_liters = 20
    sample_gallons = 40

    print(meters_to_feet(sample_meters))
    print(feet_to_meters(sample_feet))
    print(kilograms_to_pounds(sample_kilograms))
    print(pounds_to_kilograms(sample_pounds))
    print(liters_to_gallons(sample_liters))
    print(gallons_to_liters(sample_gallons))