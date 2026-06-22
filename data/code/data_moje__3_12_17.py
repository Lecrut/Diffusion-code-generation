from typing import List, Dict, Any

UNIT_FACTORS: Dict[str, Any] = {
    "celsius_to_fahrenheit_multiplier": 9.0 / 5.0,
    "celsius_to_fahrenheit_offset": 32.0
}

def convert_temperature_values(celsius_values: List[float]) -> List[float]:
    multiplier = UNIT_FACTORS["celsius_to_fahrenheit_multiplier"]
    offset = UNIT_FACTORS["celsius_to_fahrenheit_offset"]
    return [(c * multiplier) + offset for c in celsius_values]

if __name__ == '__main__':
    sample_records = [
        {"id": 1, "temp": -273.15},
        {"id": 2, "temp": 0.0},
        {"id": 3, "temp": 37.0},
        {"id": 4, "temp": 100.0},
        {"id": 5, "temp": 18.5}
    ]
    extracted_temps = [record["temp"] for record in sample_records]
    converted_temps = convert_temperature_values(extracted_temps)
    for original, converted in zip(extracted_temps, converted_temps):
        print(f"{original} C = {converted} F")