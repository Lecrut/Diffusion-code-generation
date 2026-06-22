class DistanceConversion:
    def __init__(self):
        self.factors_to_base = {
            'meter': 1.0,
            'kilometer': 1000.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'mile': 1609.344,
            'yard': 0.9144,
            'foot': 0.3048,
            'inch': 0.0254
        }
        self.inverse_factors = {k: 1.0 / v for k, v in self.factors_to_base.items()}

    def _normalize(self, unit):
        normalized = unit.strip().lower()
        if normalized not in self.factors_to_base:
            raise ValueError(f"Unsupported unit: {unit}")
        return normalized

    def convert(self, value, from_unit, to_unit):
        if value < 0:
            raise ValueError("Distance cannot be negative")
        from_norm = self._normalize(from_unit)
        to_norm = self._normalize(to_unit)
        if from_norm == to_norm:
            return value
        base_value = value * self.factors_to_base[from_norm]
        result = base_value * self.inverse_factors[to_norm]
        return result

if __name__ == '__main__':
    converter = DistanceConversion()
    result1 = converter.convert(1, 'mile', 'kilometer')
    print(result1)
    result2 = converter.convert(5280, 'foot', 'meter')
    print(result2)
    result3 = converter.convert(100, 'centimeter', 'inch')
    print(result3)