def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def grams_to_ounces(grams):
    return grams * 0.035274

def ounces_to_grams(ounces):
    return ounces / 0.035274

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

if __name__ == '__main__':
    temp_c = 100
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c} degrees Celsius is {temp_f} degrees Fahrenheit")

    temp_f_in = 32
    temp_c_out = fahrenheit_to_celsius(temp_f_in)
    print(f"{temp_f_in} degrees Fahrenheit is {temp_c_out} degrees Celsius")

    dist_km = 50
    dist_mi = kilometers_to_miles(dist_km)
    print(f"{dist_km} kilometers is {dist_mi} miles")

    dist_mi_in = 10
    dist_km_out = miles_to_kilometers(dist_mi_in)
    print(f"{dist_mi_in} miles is {dist_km_out} kilometers")

    mass_g = 500
    mass_oz = grams_to_ounces(mass_g)
    print(f"{mass_g} grams is {mass_oz} ounces")

    vol_l = 10
    vol_gal = liters_to_gallons(vol_l)
    print(f"{vol_l} liters is {vol_gal} gallons")