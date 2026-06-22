def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

if __name__ == '__main__':
    print(f"10 meters is {meters_to_feet(10):.4f} feet")
    print(f"1 kilometer is {kilometers_to_miles(1):.4f} miles")
    print(f"5 kilograms is {kilograms_to_pounds(5):.4f} pounds")
    print(f"100 celsius is {celsius_to_fahrenheit(100):.2f} fahrenheit")