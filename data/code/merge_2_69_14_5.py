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
        raise TypeError(f"Invalid input format for mass conversion: {e}") from e
    kg_value = (value_decimal * unit_factors[from_unit]) / Decimal('1000')
    if to_unit == 'g':
        return str(kg_value * 1000)
    elif to_unit == 'mg':
        return str(kg_value * 1_000_000)
    else:          
        result = kg_value / unit_factors[to_unit] if unit_factors[to_unit] != Decimal('1') else kg_value
        return str(result)
if __name__ == '__main__':
    sample_tests = [
        ('50', 'g', 'kg'),
        ('2.5', 'mg', 't'),
        ('100', 'kg', 'g'),
        ('3', 't', 'mg')
    ]
    for val, from_u, to_u in sample_tests:
        result = convert_mass(val, from_u, to_u)
        print(f"{val} {from_u} -> {result} {to_u}")