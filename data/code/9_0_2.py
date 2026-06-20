import math

class VolumeConverter:
    def __init__(self):
        self.to_liters = {
            "liter": 1.0,
            "milliliter": 0.001,
            "cubic_meter": 1000.0,
            "gallon_us": 3.785411784,
            "cubic_inch": 0.016387064
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.to_liters:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.to_liters:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        
        liters = value * self.to_liters[from_unit]
        result = liters / self.to_liters[to_unit]
        return result

    def convert_batch(self, conversions):
        results = []
        for item in conversions:
            val = item["value"]
            src = item["from"]
            tgt = item["to"]
            converted = self.convert(val, src, tgt)
            results.append({
                "original_value": val,
                "original_unit": src,
                "converted_value": converted,
                "target_unit": tgt
            })
        return results

if __name__ == "__main__":
    converter = VolumeConverter()
    
    test_cases = [
        {"value": 1, "from": "liter", "to": "milliliter"},
        {"value": 1, "from": "cubic_meter", "to": "liter"},
        {"value": 1, "from": "gallon_us", "to": "liter"},
        {"value": 100, "from": "cubic_inch", "to": "milliliter"},
        {"value": 5, "from": "gallon_us", "to": "cubic_inch"}
    ]
    
    batch_results = converter.convert_batch(test_cases)
    
    for res in batch_results:
        print(f"{res['original_value']} {res['original_unit']} = {res['converted_value']} {res['target_unit']}")