class DistanceConverter:
    def __init__(self):
        self.kilometer_to_base = 1000
        self.meter_to_base = 1
        self.centimeter_to_base = 0.01
        self.millimeter_to_base = 0.001
        self.mile_to_base = 1609.344
        self.yard_to_base = 0.9144
        self.foot_to_base = 0.3048
        self.inch_to_base = 0.0254

    def convert(self, value, from_unit, to_unit):
        if value < 0:
            raise ValueError("Distance cannot be negative")
        
        from_factors = {
            'km': self.kilometer_to_base,
            'm': self.meter_to_base,
            'cm': self.centimeter_to_base,
            'mm': self.millimeter_to_base,
            'mi': self.mile_to_base,
            'yd': self.yard_to_base,
            'ft': self.foot_to_base,
            'in': self.inch_to_base,
            'kilometer': self.kilometer_to_base,
            'meter': self.meter_to_base,
            'centimeter': self.centimeter_to_base,
            'millimeter': self.millimeter_to_base,
            'mile': self.mile_to_base,
            'yard': self.yard_to_base,
            'foot': self.foot_to_base,
            'inch': self.inch_to_base,
        }

        to_factors = {
            'km': self.kilometer_to_base,
            'm': self.meter_to_base,
            'cm': self.centimeter_to_base,
            'mm': self.millimeter_to_base,
            'mi': self.mile_to_base,
            'yd': self.yard_to_base,
            'ft': self.foot_to_base,
            'in': self.inch_to_base,
            'kilometer': self.kilometer_to_base,
            'meter': self.meter_to_base,
            'centimeter': self.centimeter_to_base,
            'millimeter': self.millimeter_to_base,
            'mile': self.mile_to_base,
            'yard': self.yard_to_base,
            'foot': self.foot_to_base,
            'inch': self.inch_to_base,
        }

        if from_unit not in from_factors:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in to_factors:
            raise ValueError(f"Unsupported target unit: {to_unit}")

        base_value = value * from_factors[from_unit]
        converted_value = base_value / to_factors[to_unit]
        
        return converted_value

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.convert(5, 'km', 'mi')
    print(result)