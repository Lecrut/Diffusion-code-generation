UNITS = {
    "ml": 1.0,
    "l": 1000.0,
    "gal": 3785.411784,
    "m3": 1000000.0,
    "ft3": 28316.846592,
}

def convert(value, from_unit, to_unit):
    base_liters = value * UNITS[from_unit]
    return base_liters / UNITS[to_unit]

if __name__ == '__main__':
    print(convert(1, "l", "ml"))
    print(convert(1, "m3", "gal"))