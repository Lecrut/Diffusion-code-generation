class VolumeConverter:
    def __init__(self):
        self._registry = {}
    def register_unit(self, unit_name, conversion_factor):
        if not isinstance(unit_name, str) or not isinstance(conversion_factor, (int, float)):
            raise ValueError("Unit name must be a string and factor must be numeric.")
        self._registry[unit_name] = conversion_factor
    def convert_from_base(self, value, source_unit, target_unit):
        if source_unit not in self._registry:
            raise KeyError(f"Unknown unit: {source_unit}")
        base_value = value * self._registry[source_unit]
        if target_unit == "base":
            return base_value
        if target_unit not in self._registry:
            raise KeyError(f"Unknown unit: {target_unit}")
        converted_value = base_value / self._registry[target_unit]
        return converted_value
    def get_available_units(self):
        return list(self._registry.keys())
if __name__ == '__main__':
    converter = VolumeConverter()
    converter.register_unit("liters", 1.0)
    converter.register_unit("milliliters", 0.001)
    converter.register_unit("gallons_usa", 3.78541)
    result_liters = converter.convert_from_base(2, "liters", "base")
    result_ml = converter.convert_from_base(2, "milliliters", "base")
    result_gallons = converter.convert_from_base(3.78541, "gallons_usa", "base")
    print(f"Converted 2 liters to base: {result_liters}")
    print(f"Converted 0.002 ml (calculated from input) to base: {result_ml}")
    print(f"Converted 378541 gallons_usa to base: {result_gallons}")
    converter.register_unit("cubic_meters", 264.172)                                                                           
    converter.register_unit("cubic_meters", 1000)
    result_cm3 = converter.convert_from_base(2, "cubic_meters", "base")
    print(f"Converted 2 cubic_meters to base: {result_cm3}")