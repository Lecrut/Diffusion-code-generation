def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

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
    sample_temp_celsius = 25
    sample_temp_fahrenheit = 77
    sample_dist_km = 10
    sample_dist_miles = 5
    sample_mass_kg = 60
    sample_mass_lbs = 150
    sample_vol_liters = 20
    sample_vol_gallons = 10
    sample_len_meters = 2
    sample_len_feet = 6

    print(celsius_to_fahrenheit(sample_temp_celsius))
    print(fahrenheit_to_celsius(sample_temp_fahrenheit))
    print(kilometers_to_miles(sample_dist_km))
    print(miles_to_kilometers(sample_dist_miles))
    print(kilograms_to_pounds(sample_mass_kg))
    print(pounds_to_kilograms(sample_mass_lbs))
    print(liters_to_gallons(sample_vol_liters))
    print(gallons_to_liters(sample_vol_gallons))
    print(meters_to_feet(sample_len_meters))
    print(feet_to_meters(sample_len_feet))