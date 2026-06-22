class LengthComparator:
    def __init__(self, unit_a, unit_b):
        self.unit_a = unit_a
        self.unit_b = unit_b

    def compare(self, value_a, value_b):
        factors = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.344,
            'ft': 0.3048,
            'in': 0.0254,
            'yd': 0.9144
        }
        
        base_unit_a = factors.get(self.unit_a, 1.0)
        base_unit_b = factors.get(self.unit_b, 1.0)
        
        value_in_meters_a = value_a * base_unit_a
        value_in_meters_b = value_b * base_unit_b
        
        if value_in_meters_a > value_in_meters_b:
            return 1
        elif value_in_meters_a < value_in_meters_b:
            return -1
        else:
            return 0

if __name__ == '__main__':
    comparator = LengthComparator('m', 'ft')
    result = comparator.compare(1, 3.28)
    print(result)