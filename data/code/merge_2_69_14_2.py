from decimal import Decimal, getcontext, InvalidOperation
getcontext().prec = 50
def convert_mass(value: str, from_unit: str, to_unit: str) -> Decimal:
    conversion_factors = {
        'gram': 1e-3,               
        'kilogram': 1.0,             
        'milligram': 1e-6,           
        'metric_ton': 1e3,          
        'pound': Decimal('453.59237'),                              
        'ounce': Decimal('0.028349523125'),                              
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
    try:
        value_decimal = Decimal(value.strip())
    except InvalidOperation as e:
        raise ValueError("Invalid numeric input for mass") from e
    factor_from = conversion_factors[from_unit]
    factor_to = conversion_factors[to_unit]
    kg_value = value_decimal * Decimal(str(factor_from)) / Decimal(str(factor_to))
    return kg_value
if __name__ == '__main__':
    test_cases = [
        ("10", "pound", "gram"),                  
        ("5.234", "metric_ton", "ounce"),                
        ("1e6", "milligram", "kilogram"),                     
        ("0.75", "pound", "gram")                   
    ]
    for value_str, from_u, to_u in test_cases:
        result = convert_mass(value_str, from_u, to_u)
        print(f"{value_str} {from_u} -> {to_u}: {result}")