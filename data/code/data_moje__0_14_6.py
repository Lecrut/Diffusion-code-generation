class LengthConverter:
    METERS_TO_OTHERS = {
        'm': 1.0,
        'km': 0.001,
        'cm': 100.0,
        'mm': 1000.0,
        'in': 39.37007874015748,
        'ft': 3.280839895013123,
        'yd': 1.093613298337708,
        'mi': 0.000621371192237334,
    }
    OTHERS_TO_METERS = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
    }

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in self.OTHERS_TO_METERS or to_unit not in self.METERS_TO_OTHERS:
            raise ValueError("Invalid unit provided")
        meters = value * self.OTHERS_TO_METERS[from_unit]
        return meters * self.METERS_TO_OTHERS[to_unit]

if __name__ == '__main__':
    converter = LengthConverter()
    result_m_to_km = converter.convert(1500, 'm', 'km')
    result_ft_to_m = converter.convert(5280, 'ft', 'm')
    result_mi_to_km = converter.convert(10, 'mi', 'km')
    result_cm_to_in = converter.convert(100, 'cm', 'in')
    print(result_m_to_km)
    print(result_ft_to_m)
    print(result_mi_to_km)
    print(result_cm_to_in)