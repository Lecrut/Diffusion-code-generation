class VolumeConverter:
    _factor_map = {
        'milliliters': 0.001,
        'liters': 1.0,
        'gallons': 3.785411784,
        'quarts': 1.1365225,
        'pints': 0.56826125,
        'cups': 0.24,
        'fluid_ounces': 0.0295735296875,
        'cubic_meters': 1000.0,
        'cubic_centimeters': 0.001,
        'cubic_inches': 0.016387064,
        'cubic_feet': 28.316846592,
        'imperial_gallons': 4.54609,
        'imperial_pints': 0.56826125,
        'imperial_cups': 0.284130625,
        'imperial_fluid_ounces': 0.0284130625,
    }

    def __init__(self, volume, from_unit='liters'):
        self.volume = volume
        self.from_unit = from_unit
        self.value_in_liters = self._convert_to_base()

    def _convert_to_base(self):
        factor = self._factor_map.get(self.from_unit)
        if factor is None:
            raise ValueError(f"Unsupported unit: {self.from_unit}")
        return self.volume * factor

    def convert_to(self, to_unit):
        if to_unit not in self._factor_map:
            raise ValueError(f"Unsupported unit: {to_unit}")
        factor = self._factor_map[to_unit]
        return self.value_in_liters / factor

    def convert_from_base(self, volume_in_liters, to_unit):
        if to_unit not in self._factor_map:
            raise ValueError(f"Unsupported unit: {to_unit}")
        factor = self._factor_map[to_unit]
        return volume_in_liters / factor

if __name__ == '__main__':
    converter = VolumeConverter(10, 'gallons')
    result_liters = converter.value_in_liters
    result_milliliters = converter.convert_to('milliliters')
    result_cups = converter.convert_to('cups')
    
    print(f"10 gallons = {result_liters} liters")
    print(f"10 gallons = {result_milliliters} milliliters")
    print(f"10 gallons = {result_cups} cups")