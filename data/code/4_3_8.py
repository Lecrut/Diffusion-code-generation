def meters_to_feet(value):
    return value * 3.28084

def feet_to_meters(value):
    return value / 3.28084

def kilometers_to_miles(value):
    return value * 0.621371

def miles_to_kilometers(value):
    return value / 0.621371

def centimeters_to_inches(value):
    return value / 2.54

def inches_to_centimeters(value):
    return value * 2.54

def liters_to_gallons(value):
    return value * 0.264172

def gallons_to_liters(value):
    return value / 0.264172

def kilograms_to_pounds(value):
    return value * 2.20462

def pounds_to_kilograms(value):
    return value / 2.20462

def celsius_to_fahrenheit(value):
    return (value * 9 / 5) + 32

def fahrenheit_to_celsius(value):
    return (value - 32) * 5 / 9

if __name__ == '__main__':
    print(meters_to_feet(100))
    print(kilometers_to_miles(5))
    print(celsius_to_fahrenheit(100))
    print(liters_to_gallons(10))
    print(kilograms_to_pounds(1))