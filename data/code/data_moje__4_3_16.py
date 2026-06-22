def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

if __name__ == '__main__':
    sample_meters = 100
    sample_feet = 328.084
    sample_kg = 70
    sample_pounds = 154.3234
    sample_celsius = 25
    sample_fahrenheit = 77
    sample_km = 10
    sample_miles = 6.21371

    print(meters_to_feet(sample_meters))
    print(feet_to_meters(sample_feet))
    print(kilograms_to_pounds(sample_kg))
    print(pounds_to_kilograms(sample_pounds))
    print(celsius_to_fahrenheit(sample_celsius))
    print(fahrenheit_to_celsius(sample_fahrenheit))
    print(kilometers_to_miles(sample_km))
    print(miles_to_kilometers(sample_miles))