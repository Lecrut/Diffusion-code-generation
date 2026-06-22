def convert_weight(value, from_unit, to_unit):
    conversion_factors = {'kg': 1.0, 'lb': 2.20462, 'g': 1000.0, 'oz': 35.2739}
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError('Invalid unit provided.')
    value_in_base = value * conversion_factors[from_unit]
    result = value_in_base / conversion_factors[to_unit]
    return result
if __name__ == '__main__':
    kg_to_lb = convert_weight(1, 'kg', 'lb')
    lb_to_kg = convert_weight(2.20462, 'lb', 'kg')
    g_to_oz = convert_weight(35.2739, 'g', 'oz')
    print(kg_to_lb)
    print(lb_to_kg)
    print(g_to_oz)