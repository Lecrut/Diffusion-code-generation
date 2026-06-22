from typing import Union

def convert_length(value: float) -> dict:
    return {
        "kilometers": value,
        "meters": value * 1000,
        "miles": value / 1.60934,
        "feet": value * 3280.84
    }

def convert_mass(value: float) -> dict:
    return {
        "kilograms": value,
        "grams": value * 1000,
        "pounds": value / 0.453592,
        "ounces": value * 35.274
    }

def convert_distance(value: float) -> dict:
    return {
        "kilometers": value,
        "meters": value * 1000,
        "miles": value / 1.60934,
        "feet": value * 3280.84
    }

def convert_temperature(value: float) -> dict:
    return {
        "celsius": value,
        "fahrenheit": value * 9/5 + 32,
        "kelvin": value + 273.15
    }

if __name__ == '__main__':
    length_result = convert_length(1)
    print(length_result)

    mass_result = convert_mass(1)
    print(mass_result)

    distance_result = convert_distance(1)
    print(distance_result)

    temperature_result = convert_temperature(100)
    print(temperature_result)