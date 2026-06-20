def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

if __name__ == '__main__':
    print(meters_to_feet(1))
    print(feet_to_meters(1))
    print(kilograms_to_pounds(1))
    print(pounds_to_kilograms(1))
    print(celsius_to_fahrenheit(0))
    print(fahrenheit_to_celsius(32))
    print(kilometers_to_miles(1))
    print(miles_to_kilometers(1))