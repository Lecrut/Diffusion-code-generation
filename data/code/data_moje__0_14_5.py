import sys

class UnitConverter:
    _METERS_FACTORS = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.344
    }

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit not in self._METERS_FACTORS:
            raise ValueError(f"Invalid source unit: {from_unit}")
        if to_unit not in self._METERS_FACTORS:
            raise ValueError(f"Invalid target unit: {to_unit}")
        meters = value * self._METERS_FACTORS[from_unit]
        return meters / self._METERS_FACTORS[to_unit]

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.convert(1000, 'meters', 'kilometers'))
    print(converter.convert(1, 'mile', 'meters'))
    print(converter.convert(12, 'inches', 'feet'))
    print(converter.convert(5, 'feet', 'centimeters'))
    print(converter.convert(100, 'centimeters', 'inches'))
    print(converter.convert(1, 'yard', 'meters'))
    print(converter.convert(10000, 'millimeters', 'miles'))
    print(converter.convert(1, 'kilometer', 'yards'))
    sys.exit(0)