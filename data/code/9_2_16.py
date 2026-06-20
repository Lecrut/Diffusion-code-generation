def convert_volume(value, target_unit):
    units = {
        'm3': 1.0,
        'L': 1000.0,
        'gal': 264.1720523581,
        'pt': 2113.3764188652,
        'qt': 1056.6882094326,
        'cup': 4226.7528377304,
        'tbsp': 67628.045403696,
        'tsp': 202884.13621109,
        'in3': 61023.744094732,
        'ft3': 35.3146667215,
        'oz': 33814.022702,
    }
    if target_unit not in units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    liters = value * units['L']
    return liters / units[target_unit]

if __name__ == '__main__':
    print(convert_volume(1, 'gal'))
    print(convert_volume(1, 'm3'))
    print(convert_volume(10, 'L'))