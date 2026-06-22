import argparse

VOLUME_UNITS = {
    "ml": {"name": "milliliter", "to_liters": 0.001},
    "l": {"name": "liter", "to_liters": 1.0},
    "gal": {"name": "gallon", "to_liters": 3.78541},
    "qt": {"name": "quart", "to_liters": 0.946353},
    "pt": {"name": "pint", "to_liters": 0.473176},
    "cup": {"name": "cup", "to_liters": 0.236588},
    "fl_oz": {"name": "fluid_ounce", "to_liters": 0.0295735},
    "tbsp": {"name": "tablespoon", "to_liters": 0.0147868},
    "tsp": {"name": "teaspoon", "to_liters": 0.00492892},
    "m3": {"name": "cubic_meter", "to_liters": 1000.0},
}

def convert_volume(volume, from_unit, to_unit):
    if from_unit not in VOLUME_UNITS:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit not in VOLUME_UNITS:
        raise ValueError(f"Unknown target unit: {to_unit}")

    liters = volume * VOLUME_UNITS[from_unit]["to_liters"]
    result = liters / VOLUME_UNITS[to_unit]["to_liters"]
    return result

def create_parser():
    parser = argparse.ArgumentParser(description="Convert volume between units.")
    parser.add_argument("volume", type=float, help="The volume to convert")
    parser.add_argument("from_unit", type=str, help="The starting unit")
    parser.add_argument("to_unit", type=str, help="The target unit")
    return parser

def main():
    volume = 1.0
    from_unit = "gal"
    to_unit = "l"
    result = convert_volume(volume, from_unit, to_unit)
    print(result)

if __name__ == '__main__':
    main()