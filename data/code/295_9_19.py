conversion_factors = {
    'kg_to_lbs': 2.20462,
    'lbs_to_kg': 1 / 2.20462
}

def get_conversion_factor(from_unit, to_unit):
    return conversion_factors.get(f'{from_unit}_to_{to_unit}')

if __name__ == '__main__':
    factor = get_conversion_factor('kg', 'lbs')
    print(f"Conversion factor from kg to lbs: {factor:.2f}")