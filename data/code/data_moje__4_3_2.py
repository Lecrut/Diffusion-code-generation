def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

if __name__ == '__main__':
    sample_length_m = 100
    print(meters_to_feet(sample_length_m))
    print(feet_to_meters(meters_to_feet(sample_length_m)))

    sample_weight_kg = 70
    print(kilograms_to_pounds(sample_weight_kg))
    print(pounds_to_kilograms(kilograms_to_pounds(sample_weight_kg)))

    sample_temp_c = 25
    print(celsius_to_fahrenheit(sample_temp_c))
    print(fahrenheit_to_celsius(celsius_to_fahrenheit(sample_temp_c)))

    sample_distance_km = 50
    print(kilometers_to_miles(sample_distance_km))
    print(miles_to_kilometers(kilometers_to_miles(sample_distance_km)))

    sample_volume_l = 5
    print(liters_to_gallons(sample_volume_l))
    print(gallons_to_liters(liters_to_gallons(sample_volume_l)))