from decimal import Decimal, getcontext
getcontext().prec = 50
def convert_mass(value: str, from_unit: str, to_unit: str) -> Decimal:
    unit_factors = {
        'g': Decimal('1'),                              
        'mg': Decimal('0.001'),                                 
        'kg': Decimal('1'),                             
        't': Decimal('1000'),                           
    }
    if from_unit not in unit_factors or to_unit not in unit_factors:
        raise ValueError(f"Unsupported units. Available: {list(unit_factors.keys())}")
    try:
        value_decimal = Decimal(value)
    except Exception as e:
        raise TypeError(f"Invalid input format for mass value: {e}") from e
    kg_value = value_decimal * unit_factors[from_unit] / unit_factors[to_unit]
    return kg_value
if __name__ == '__main__':
    sample_input_1 = "50"
    from_units_list = ['g', 'mg', 'kg']
    to_units_list = ['t', 'kg', 'g']
    test_cases = [
        (sample_input_1, 'g', 't'),
        ("250", "mg", "kg"),
        ("3.5", "kg", "g")
    ]
    for val_str, src_unit, dst_unit in test_cases:
        result = convert_mass(val_str, src_unit, dst_unit)
        print(f"{val_str} {src_unit} -> {result} {dst_unit}")