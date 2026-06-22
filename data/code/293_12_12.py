from typing import Union

def convert_length(meters: float) -> dict:
    kilometers = meters / 1000
    miles = meters * 0.000621371
    feet = meters * 3.28084
    return {
        "meters": meters,
        "kilometers": kilometers,
        "miles": miles,
        "feet": feet
    }

def convert_mass(kilograms: float) -> dict:
    pounds = kilograms * 2.20462
    ounces = kilograms * 35.274
    return {
        "kilograms": kilograms,
        "pounds": pounds,
        "ounces": ounces
    }

if __name__ == '__main__':
    length_result = convert_length(1000)
    mass_result = convert_mass(1)

    print("Length Conversion:", length_result)
    print("Mass Conversion:", mass_result)