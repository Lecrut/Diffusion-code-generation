from decimal import Decimal, getcontext, InvalidOperation
getcontext().prec = 50
def convert_mass(value: str, from_unit: str, to_unit: str) -> Decimal:
    unit_factors = {
        'kilogram': Decimal('1'),
        'gram': Decimal('0.001'),
        'milligram': Decimal('0.000001'),
        'microgram': Decimal('0.000000001'),
        'pound': Decimal('0.45359237'),
        'ounce': Decimal('0.028349523125'),
    }
    if from_unit not in unit_factors or to_unit not in unit_factors:
        raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
    try:
        value_decimal = Decimal(value.strip())
    except InvalidOperation as e:
        raise ValueError(f"Invalid numeric input for mass conversion: {e}") from e
    kg_value = value_decimal * unit_factors[from_unit]
    result_kg = kg_value / unit_factors[to_unit]
    return result_kg
if __name__ == '__main__':
    sample_values = [
        ('10', 'kilogram', 'gram'),
        ('5.2', 'pound', 'ounce'),
        ('1000', 'milligram', 'microgram'),
        ('0.75', 'ounce', 'kilogram')
    ]
    for val_str, from_u, to_u in sample_values:
        result = convert_mass(val_str, from_u, to_u)
        print(f"{val_str} {from_u} -> {result}")