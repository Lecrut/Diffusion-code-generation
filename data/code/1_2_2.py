import re
from decimal import Decimal, InvalidOperation

class WeightConverter:
    def __init__(self):
        self.conversion_factors = {
            'kg': 1.0,
            'kilogram': 1.0,
            'kilograms': 1.0,
            'g': 0.001,
            'gram': 0.001,
            'grams': 0.001,
            'lb': 0.45359237,
            'lbs': 0.45359237,
            'pound': 0.45359237,
            'pounds': 0.45359237,
            'oz': 0.028349523125,
            'ounce': 0.028349523125,
            'ounces': 0.028349523125,
            'st': 6.35029318,
            'stone': 6.35029318,
            'stones': 6.35029318,
            't': 1000.0,
            'ton': 1000.0,
            'tonne': 1000.0,
        }

    def convert_measurement(self, measurement):
        pattern = r'^\s*([+-]?\d*\.?\d+(?:e[+-]?\d+)?)\s*(kg|kilogram|kilograms|g|gram|grams|lb|lbs|pound|pounds|oz|ounce|ounces|st|stone|stones|t|ton|tonne)\s*$'
        match = re.match(pattern, measurement, re.IGNORECASE)
        if not match:
            raise ValueError(f"Invalid format: '{measurement}'")
        
        try:
            value = float(match.group(1))
        except ValueError:
            raise ValueError(f"Invalid number: '{match.group(1)}'")
        
        unit = match.group(2).lower()
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: '{unit}'")
        
        factor = self.conversion_factors[unit]
        return value * factor

    def convert_list(self, measurements):
        results = []
        for m in measurements:
            try:
                result = self.convert_measurement(m)
                results.append((m, result))
            except ValueError as e:
                results.append((m, str(e)))
        return results

def convert_weight_measurements(measurements):
    converter = WeightConverter()
    return converter.convert_list(measurements)

if __name__ == '__main__':
    sample_measurements = [
        "1.5 kg",
        "100 g",
        "2 lb",
        "16 oz",
        "1 stone",
        "invalid input",
        "500",
        "-2.5 lbs"
    ]
    results = convert_weight_measurements(sample_measurements)
    for original, result in results:
        if isinstance(result, float):
            print(f"{original} -> {result:.6f} kg")
        else:
            print(f"{original} -> Error: {result}")