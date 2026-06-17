import math
def convert_length(value, unit):
    if unit in ['m', 'meter', 'meters']:
        if unit == 'm':
            return value
        elif unit == 'meter':
            return value
        elif unit == 'meters':
            return value
    elif unit in ['km', 'kilometer', 'kilometers']:
        if unit == 'km':
            return value * 1000
        elif unit == 'kilometer':
            return value * 1000
        elif unit == 'kilometers':
            return value * 1000
    elif unit in ['ft', 'foot', 'feet']:
        if unit == 'ft':
            return value * 0.3048
        elif unit == 'foot':
            return value * 0.3048
        elif unit == 'feet':
            return value * 0.3048
    elif unit in ['mi', 'mile', 'miles']:
        if unit == 'mi':
            return value * 1609.344
        elif unit == 'mile':
            return value * 1609.344
        elif unit == 'miles':
            return value * 1609.344
    return None
def convert_mass(value, unit):
    if unit in ['g', 'gram', 'grams']:
        if unit == 'g':
            return value
        elif unit == 'gram':
            return value
        elif unit == 'grams':
            return value
    elif unit in ['kg', 'kilogram', 'kilograms']:
        if unit == 'kg':
            return value
        elif unit == 'kilogram':
            return value
        elif unit == 'kilograms':
            return value
    elif unit in ['lb', 'pound', 'pounds']:
        if unit == 'lb':
            return value * 453.592
        elif unit == 'pound':
            return value * 453.592
        elif unit == 'pounds':
            return value * 453.592
    elif unit in ['oz', 'ounce', 'ounces']:
        if unit == 'oz':
            return value * 28.3495
        elif unit == 'ounce':
            return value * 28.3495
        elif unit == 'ounces':
            return value * 28.3495
    return None
if __name__ == '__main__':
    print("--- Length Conversions ---")
    sample_length = 10
    sample_length_m = sample_length * 1000
    sample_length_ft = sample_length * 3.28084
    sample_length_mi = sample_length * 0.000621371
    print(f"Sample Length: {sample_length} meters")
    print(f"{sample_length} m -> {convert_length(sample_length, 'm')} m")
    print(f"{sample_length} m -> {convert_length(sample_length, 'km')} km")
    print(f"{sample_length} m -> {convert_length(sample_length, 'ft')} ft")
    print(f"{sample_length} m -> {convert_length(sample_length, 'mi')} mi\n")
    print("--- Mass Conversions ---")
    sample_mass = 500
    sample_mass_kg = sample_mass / 1000
    sample_mass_lb = sample_mass * 2.2046226
    sample_mass_oz = sample_mass * 35.27395
    print(f"Sample Mass: {sample_mass} grams")
    print(f"{sample_mass} g -> {convert_mass(sample_mass, 'kg')} kg")
    print(f"{sample_mass} g -> {convert_mass(sample_mass, 'lb')} lb")
    print(f"{sample_mass} g -> {convert_mass(sample_mass, 'oz')} oz")