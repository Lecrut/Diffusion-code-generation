import math
def convert_mass_units(mass, source_unit):
    conversions = {}
    if source_unit == 'kg':
        conversions['kg'] = mass
        conversions['g'] = mass * 1000
        conversions['lb'] = mass * 2.204622
    elif source_unit == 'g':
        conversions['g'] = mass
        conversions['kg'] = mass / 1000
        conversions['lb'] = mass * 0.002204622
    elif source_unit == 'lb':
        conversions['lb'] = mass
        conversions['kg'] = mass / 2.204622
        conversions['g'] = mass * 453.59237
    else:
        return {"error": "Unsupported source unit"}
    return conversions
if __name__ == '__main__':
    mass_value = 10
    source = 'kg'
    results = convert_mass_units(mass_value, source)
    print(f"Source Mass: {mass_value} {source}")
    for unit, converted_value in results.items():
        if unit != source:
            print(f"{unit}: {converted_value:.4f}")