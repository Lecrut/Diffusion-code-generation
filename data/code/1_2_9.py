import re
from decimal import Decimal, InvalidOperation

def convert_to_kilograms(measurements):
    results = []
    for item in measurements:
        try:
            if not isinstance(item, str):
                raise ValueError("Measurement must be a string")
            
            pattern = r'^\s*([+-]?\d+\.?\d*)\s*(kg|g|lb|oz|t)\s*$'
            match = re.match(pattern, item, re.IGNORECASE)
            
            if not match:
                raise ValueError(f"Invalid format: {item}")
            
            value_str, unit = match.groups()
            value = Decimal(value_str)
            unit = unit.lower()
            
            conversion_factors = {
                'kg': Decimal('1'),
                'g': Decimal('0.001'),
                'lb': Decimal('0.45359237'),
                'oz': Decimal('0.028349523125'),
                't': Decimal('1000')
            }
            
            factor = conversion_factors.get(unit)
            if factor is None:
                raise ValueError(f"Unknown unit: {unit}")
            
            result = value * factor
            results.append(float(result))
            
        except Exception:
            results.append(None)
    
    return results

if __name__ == '__main__':
    sample_data = ["5kg", "1000g", "2.2lb", "16oz", "0.5t", "invalid", "10xyz", "-3kg"]
    output = convert_to_kilograms(sample_data)
    print(output)