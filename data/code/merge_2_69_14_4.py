import decimal
def convert_mass(value: float, from_unit: str, to_unit: str) -> decimal.Decimal:
    unit_factors = {
        'g': 1e-3,                    
        'mg': 1e-6,                        
        'kg': 1.0,                        
        't': 1e3,                               
    }
    if from_unit not in unit_factors or to_unit not in unit_factors:
        raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
    factor_from = decimal.Decimal(unit_factors[from_unit])
    factor_to = decimal.Decimal(unit_factors[to_unit])
    ctx = decimal.getcontext()
    ctx.prec = 50
    value_decimal = decimal.Decimal(value)
    intermediate_kg = value_decimal * factor_from
    final_value = intermediate_kg * factor_to
    return final_value
if __name__ == '__main__':
    test_cases = [
        (50.1234, 'mg', 'kg'),
        (1e9, 't', 'g'),
        (2.5, 'kg', 'mg')
    ]
    for mass_val, start_unit, end_unit in test_cases:
        result = convert_mass(mass_val, start_unit, end_unit)
        print(f"{mass_val} {start_unit} -> {result}")