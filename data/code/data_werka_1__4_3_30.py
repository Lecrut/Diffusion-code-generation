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
    print('5 meters to feet:', meters_to_feet(5))
    print('10 feet to meters:', feet_to_meters(10))
    print('100 kilograms to pounds:', kilograms_to_pounds(100))
    print('200 pounds to kilograms:', pounds_to_kilograms(200))
    print('10 liters to gallons:', liters_to_gallons(10))
    print('5 gallons to liters:', gallons_to_liters(5))