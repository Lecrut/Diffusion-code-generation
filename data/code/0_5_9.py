class UnitConverter:
    def __init__(self):
        self._conversion_factors = {}
        self._base_units = {}

    def register_unit(self, unit_name, factor_to_base):
        self._conversion_factors[unit_name] = factor_to_base

    def set_base_unit(self, unit_name):
        self._base_units[unit_name] = True

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self._conversion_factors:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self._conversion_factors:
            raise ValueError(f"Unknown unit: {to_unit}")

        from_factor = self._conversion_factors[from_unit]
        to_factor = self._conversion_factors[to_unit]

        if to_factor == 0:
            raise ZeroDivisionError("Cannot convert to a unit with zero conversion factor")

        value_in_base = value * from_factor
        result = value_in_base / to_factor

        return result

    def add_custom_conversion(self, from_unit, to_unit, factor):
        if from_unit not in self._conversion_factors:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in self._conversion_factors:
            raise ValueError(f"Unknown unit: {to_unit}")

        base_unit = next(iter(self._base_units))
        if base_unit not in self._conversion_factors:
            raise ValueError("No base unit registered")

        from_factor = self._conversion_factors[from_unit]
        to_factor = self._conversion_factors[to_unit]
        base_factor = self._conversion_factors[base_unit]

        if from_factor != base_factor or to_factor != base_factor:
            self._conversion_factors[to_unit] = from_factor / factor

def create_converter():
    converter = UnitConverter()
    converter.register_unit("meter", 1.0)
    converter.set_base_unit("meter")
    converter.register_unit("kilometer", 1000.0)
    converter.register_unit("centimeter", 0.01)
    converter.register_unit("millimeter", 0.001)
    converter.register_unit("inch", 0.0254)
    converter.register_unit("foot", 0.3048)
    converter.register_unit("yard", 0.9144)
    converter.register_unit("mile", 1609.34)
    converter.register_unit("lightyear", 9.461e15)
    return converter

if __name__ == "__main__":
    converter = create_converter()
    print(converter.convert(1, "kilometer", "meter"))
    print(converter.convert(1, "mile", "kilometer"))
    print(converter.convert(1, "foot", "inch"))
    print(converter.convert(100, "centimeter", "meter"))
    print(converter.convert(1, "lightyear", "kilometer"))
    print(converter.convert(1, "inch", "millimeter"))
    print(converter.convert(1, "yard", "foot"))
    print(converter.convert(1, "meter", "millimeter"))
    print(converter.convert(1, "kilometer", "mile"))
    print(converter.convert(1, "lightyear", "mile"))