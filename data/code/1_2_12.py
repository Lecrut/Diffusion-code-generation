import re

class WeightMeasurement:
    def __init__(self, value: str):
        self.raw_value = value
        self.value = None
        self.unit = None
        self._parse()

    def _parse(self):
        pattern = r'^\s*([+-]?\d*\.?\d+(?:[eE][+-]?\d+)?)\s*(kg|kilograms?|g|grams?|lb|lbs|pounds?|oz|ounces?|ton|tons?|mt|metric\stons?)\s*$'
        match = re.match(pattern, self.raw_value, re.IGNORECASE)
        if match:
            self.value = float(match.group(1))
            self.unit = match.group(2).lower()
        else:
            raise ValueError(f"Invalid format: '{self.raw_value}'")

    def to_kg(self) -> float:
        if self.value is None:
            return 0.0
        
        unit = self.unit
        if unit in ('kg', 'kilogram', 'kilograms'):
            return self.value
        elif unit in ('g', 'gram', 'grams'):
            return self.value / 1000.0
        elif unit in ('lb', 'lbs', 'pound', 'pounds'):
            return self.value * 0.45359237
        elif unit in ('oz', 'ounce', 'ounces'):
            return self.value * 0.028349523125
        elif unit in ('ton', 'tons'):
            return self.value * 907.18474
        elif unit in ('mt', 'metric ton', 'metric tons'):
            return self.value * 1000.0
        else:
            raise ValueError(f"Unknown unit: {self.unit}")

def convert_measurements_to_kg(measurements: list) -> list:
    results = []
    for m in measurements:
        try:
            obj = WeightMeasurement(m)
            results.append(obj.to_kg())
        except ValueError as e:
            results.append(f"Error: {str(e)}")
    return results

if __name__ == '__main__':
    sample_data = [
        "1000 g",
        "2.5 kg",
        "10 lbs",
        "16 oz",
        "invalid string",
        "1 ton",
        "0.5 mt"
    ]
    
    output = convert_measurements_to_kg(sample_data)
    print(output)