class LengthComparator:
    def __init__(self, unit_a, value_a, unit_b, value_b):
        self.unit_a = unit_a
        self.value_a = value_a
        self.unit_b = unit_b
        self.value_b = value_b
        self.conversion_rates = {
            "m": 1.0,
            "ft": 0.3048,
            "cm": 0.01,
            "mm": 0.001,
            "in": 0.0254,
            "yd": 0.9144
        }

    def _to_meters(self, value, unit):
        if unit not in self.conversion_rates:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * self.conversion_rates[unit]

    def compare(self):
        val_a_meters = self._to_meters(self.value_a, self.unit_a)
        val_b_meters = self._to_meters(self.value_b, self.unit_b)
        
        diff = val_a_meters - val_b_meters
        
        if diff > 1e-9:
            result = f"{self.value_a} {self.unit_a} is greater than {self.value_b} {self.unit_b}"
        elif diff < -1e-9:
            result = f"{self.value_a} {self.unit_a} is less than {self.value_b} {self.unit_b}"
        else:
            result = f"{self.value_a} {self.unit_a} is equal to {self.value_b} {self.unit_b}"
            
        return result

if __name__ == '__main__':
    comp = LengthComparator("m", 2.5, "ft", 8.2)
    print(comp.compare())
    
    comp2 = LengthComparator("cm", 100, "m", 1.0)
    print(comp2.compare())
    
    comp3 = LengthComparator("in", 10, "cm", 25.4)
    print(comp3.compare())