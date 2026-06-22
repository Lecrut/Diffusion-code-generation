def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def meters_to_inches(meters):
    return meters * 39.3701

def inches_to_meters(inches):
    return inches / 39.3701

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

if __name__ == '__main__':
    celsius_val = 25
    fahrenheit_val = 77
    meters_val = 10
    inches_val = 50
    kilograms_val = 5
    pounds_val = 10
    liters_val = 20
    gallons_val = 5

    print(celsius_to_fahrenheit(celsius_val))
    print(fahrenheit_to_celsius(fahrenheit_val))
    print(meters_to_inches(meters_val))
    print(inches_to_meters(inches_val))
    print(kilograms_to_pounds(kilograms_val))
    print(pounds_to_kilograms(pounds_val))
    print(liters_to_gallons(liters_val))
    print(gallons_to_liters(gallons_val))