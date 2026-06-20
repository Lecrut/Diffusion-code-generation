CONVERSION_FACTORS = {
    "meter": 1.0,
    "kilometer": 1000.0,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344
}

UNIT_ALIASES = {
    "m": "meter",
    "km": "kilometer",
    "cm": "centimeter",
    "mm": "millimeter",
    "in": "inch",
    "ft": "foot",
    "y": "yard",
    "yd": "yard",
    "mi": "mile"
}

def normalize_unit(unit):
    lower_unit = unit.lower()
    if lower_unit in CONVERSION_FACTORS:
        return lower_unit
    if lower_unit in UNIT_ALIASES:
        return UNIT_ALIASES[lower_unit]
    raise ValueError(f"Unsupported unit: {unit}")

def convert_length(value, from_unit, to_unit):
    from_key = normalize_unit(from_unit)
    to_key = normalize_unit(to_unit)
    base_meters = value * CONVERSION_FACTORS[from_key]
    return base_meters / CONVERSION_FACTORS[to_key]

class LengthConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = normalize_unit(unit)
        self.base_meters = value * CONVERSION_FACTORS[self.unit]

    def convert_to(self, target_unit):
        target_key = normalize_unit(target_unit)
        return self.base_meters / CONVERSION_FACTORS[target_key]

    def get_all_conversions(self):
        results = {}
        for unit_name in CONVERSION_FACTORS:
            results[unit_name] = self.base_meters / CONVERSION_FACTORS[unit_name]
        return results

if __name__ == '__main__':
    sample_value = 1.0
    sample_source = "mile"
    sample_target = "meter"
    
    direct_result = convert_length(sample_value, sample_source, sample_target)
    print(f"{sample_value} {sample_source} to {sample_target}: {direct_result}")
    
    converter = LengthConverter(100, "centimeter")
    converted_feet = converter.convert_to("foot")
    print(f"100 centimeters to feet: {converted_feet}")
    
    all_conversions = converter.get_all_conversions()
    print(f"100 centimeters in yards: {all_conversions['yard']}")