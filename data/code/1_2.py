import re
from decimal import Decimal, InvalidOperation

class WeightConverter:
    SUPPORTED_UNITS = {
        'kg': 1.0,
        'kilogram': 1.0,
        'kilograms': 1.0,
        'g': 0.001,
        'gram': 0.001,
        'grams': 0.001,
        'mg': 0.000001,
        'milligram': 0.000001,
        'milligrams': 0.000001,
        'lb': 0.45359237,
        'lbm': 0.45359237,
        'pound': 0.45359237,
        'pounds': 0.45359237,
        'oz': 0.028349523125,
        'ounce': 0.028349523125,
        'ounces': 0.028349523125,
        'st': 6.35029318,
        'stone': 6.35029318,
        'stones': 6.35029318,
        't': 1000.0,
        'metric ton': 1000.0,
        'tonne': 1000.0,
        'tonnes': 1000.0,
        'ton': 907.18474,
        'tons': 907.18474,
    }

    @staticmethod
    def parse_measurement(measurement_str):
        pattern = r'^\s*([+-]?\d+(?:\.\d+)?)\s*([a-zA-Z]+)\s*$'
        match = re.match(pattern, str(measurement_str).strip())
        if not match:
            raise ValueError(f"Invalid measurement format: {measurement_str}")
        value_str = match.group(1)
        unit_str = match.group(2).lower()
        
        try:
            value = float(value_str)
        except ValueError:
            raise ValueError(f"Invalid numeric value: {value_str}")
        
        if unit_str not in WeightConverter.SUPPORTED_UNITS:
            raise ValueError(f"Unsupported unit: {unit_str}")
        
        return value, unit_str

    @staticmethod
    def convert_to_kg(measurement_str):
        value, unit_str = WeightConverter.parse_measurement(measurement_str)
        conversion_factor = WeightConverter.SUPPORTED_UNITS[unit_str]
        return value * conversion_factor

    @staticmethod
    def convert_list(measurements):
        results = []
        for item in measurements:
            try:
                kg_value = WeightConverter.convert_to_kg(item)
                results.append(kg_value)
            except ValueError as e:
                results.append(f"Error: {str(e)}")
        return results

if __name__ == '__main__':
    sample_measurements = [
        "1.5 kg",
        "500 g",
        "2 lb",
        "16 oz",
        "100 mg",
        "14 stone",
        "invalid entry",
        "3.5T",
        "1000 tons",
        "abc def",
        "2.0 lbm"
    ]
    
    output = WeightConverter.convert_list(sample_measurements)
    for original, converted in zip(sample_measurements, output):
        print(f"{original} -> {converted}")