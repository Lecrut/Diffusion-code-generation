class UnitConverter:
    TO_METERS = {
        "meter": 1.0,
        "meters": 1.0,
        "meter": 1.0,
        "foot": 0.3048,
        "feet": 0.3048,
        "inch": 0.0254,
        "inches": 0.0254,
        "yard": 0.9144,
        "yards": 0.9144,
        "mile": 1609.344,
        "miles": 1609.344,
        "kilometer": 1000.0,
        "kilometers": 1000.0,
        "centimeter": 0.01,
        "centimeters": 0.01,
        "millimeter": 0.001,
        "millimeters": 0.001,
        "nautical mile": 1852.0,
        "nautical miles": 1852.0,
    }

    def __init__(self, distance, source_unit, target_unit):
        if distance < 0:
            raise ValueError("Distance cannot be negative")
        if not source_unit or not target_unit:
            raise ValueError("Source and target units cannot be empty")
        
        source_lower = source_unit.lower().strip()
        target_lower = target_unit.lower().strip()
        
        if source_lower not in self.TO_METERS:
            raise ValueError(f"Unsupported source unit: {source_unit}")
        if target_lower not in self.TO_METERS:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        self.distance = distance
        self.source_unit = source_lower
        self.target_unit = target_lower

    def convert(self):
        meters = self.distance * self.TO_METERS[self.source_unit]
        result = meters / self.TO_METERS[self.target_unit]
        return result

    def get_formatted_result(self):
        result = self.convert()
        if result == int(result):
            return f"{int(result)} {self.target_unit}"
        return f"{result:.4f} {self.target_unit}"

if __name__ == '__main__':
    sample_converter = UnitConverter(1.0, "mile", "kilometers")
    print(sample_converter.get_formatted_result())
    
    sample_converter_feet = UnitConverter(5280.0, "feet", "miles")
    print(sample_converter_feet.get_formatted_result())
    
    sample_converter_inch = UnitConverter(1.0, "inch", "centimeters")
    print(sample_converter_inch.get_formatted_result())
    
    try:
        invalid_converter = UnitConverter(10.0, "parsec", "lightyears")
    except ValueError as e:
        print(e)
    
    try:
        negative_converter = UnitConverter(-5.0, "meter", "foot")
    except ValueError as e:
        print(e)