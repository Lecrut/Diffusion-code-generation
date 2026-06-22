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

def centimeters_to_inches(centimeters):
    return centimeters / 2.54

def inches_to_centimeters(inches):
    return inches * 2.54

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

if __name__ == '__main__':
    result = meters_to_feet(1.0)
    print(result)
    result = kilograms_to_pounds(1.0)
    print(result)
    result = liters_to_gallons(1.0)
    print(result)
    result = centimeters_to_inches(1.0)
    print(result)
    result = kilometers_to_miles(1.0)
    print(result)