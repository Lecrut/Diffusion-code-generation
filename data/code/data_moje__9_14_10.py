class VolumeConverter:
    FACTORS = {
        'liters': 1.0,
        'milliliters': 1000.0,
        'gallons': 0.2641720523581484,
        'quarts': 1.0566882094325916,
        'pints': 2.1133764188651832,
        'cups': 4.226752837730366,
        'fluid_ounces': 33.814022701843136
    }

    def __init__(self):
        self.units = list(self.FACTORS.keys())

    def _to_liters(self, value, from_unit):
        from_unit = from_unit.lower()
        if from_unit == 'milliliters':
            return value / 1000.0
        elif from_unit == 'liters':
            return value
        elif from_unit == 'gallons':
            return value / 0.2641720523581484
        elif from_unit == 'quarts':
            return value / 1.0566882094325916
        elif from_unit == 'pints':
            return value / 2.1133764188651832
        elif from_unit == 'cups':
            return value / 4.226752837730366
        elif from_unit == 'fluid_ounces':
            return value / 33.814022701843136
        else:
            raise ValueError(f"Unsupported unit: {from_unit}")

    def _from_liters(self, liters, to_unit):
        to_unit = to_unit.lower()
        if to_unit == 'milliliters':
            return liters * 1000.0
        elif to_unit == 'liters':
            return liters
        elif to_unit == 'gallons':
            return liters * 0.2641720523581484
        elif to_unit == 'quarts':
            return liters * 1.0566882094325916
        elif to_unit == 'pints':
            return liters * 2.1133764188651832
        elif to_unit == 'cups':
            return liters * 4.226752837730366
        elif to_unit == 'fluid_ounces':
            return liters * 33.814022701843136
        else:
            raise ValueError(f"Unsupported unit: {to_unit}")

    def convert(self, value, from_unit, to_unit):
        liters = self._to_liters(value, from_unit)
        return self._from_liters(liters, to_unit)

    def convert_all(self, value, from_unit):
        result = {}
        liters = self._to_liters(value, from_unit)
        for unit in self.units:
            result[unit] = self._from_liters(liters, unit)
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    value = 2.5
    from_unit = 'liters'
    to_unit = 'gallons'
    result = converter.convert(value, from_unit, to_unit)
    print(result)
    all_results = converter.convert_all(1.0, 'gallons')
    for unit, converted_value in all_results.items():
        print(f"1.0 gallons = {converted_value} {unit}")