def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

if __name__ == '__main__':
    sample_meters = 100
    sample_kilograms = 50
    sample_celsius = 20
    sample_kilometers = 10
    sample_liters = 5

    print(meters_to_feet(sample_meters))
    print(feet_to_meters(meters_to_feet(sample_meters)))
    print(kilograms_to_pounds(sample_kilograms))
    print(pounds_to_kilograms(kilograms_to_pounds(sample_kilograms)))
    print(celsius_to_fahrenheit(sample_celsius))
    print(fahrenheit_to_celsius(celsius_to_fahrenheit(sample_celsius)))
    print(kilometers_to_miles(sample_kilometers))
    print(miles_to_kilometers(kilometers_to_miles(sample_kilometers)))
    print(liters_to_gallons(sample_liters))
    print(gallons_to_liters(liters_to_gallons(sample_liters)))