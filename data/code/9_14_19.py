class VolumeConverter:
    LITER_TO_MILLILITER = 1000.0
    LITER_TO_GALLON = 0.264172052
    LITER_TO_QUART = 1.05668821
    LITER_TO_PINT = 2.11337642
    LITER_TO_CUP = 4.22675284
    LITER_TO_FLUID_OUNCE = 33.8140227

    MILLILITER_TO_LITER = 1.0 / LITER_TO_MILLILITER
    GALLON_TO_LITER = 1.0 / LITER_TO_GALLON
    QUART_TO_LITER = 1.0 / LITER_TO_QUART
    PINT_TO_LITER = 1.0 / LITER_TO_PINT
    CUP_TO_LITER = 1.0 / LITER_TO_CUP
    FLUID_OUNCE_TO_LITER = 1.0 / LITER_TO_FLUID_OUNCE

    def __init__(self):
        self.conversion_factors = {
            'liter': 1.0,
            'milliliter': 1.0 / self.LITER_TO_MILLILITER,
            'gallon': 1.0 / self.LITER_TO_GALLON,
            'quart': 1.0 / self.LITER_TO_QUART,
            'pint': 1.0 / self.LITER_TO_PINT,
            'cup': 1.0 / self.LITER_TO_CUP,
            'fluid_ounce': 1.0 / self.LITER_TO_FLUID_OUNCE,
        }

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower().strip()
        to_unit = to_unit.lower().strip()
        if from_unit not in self.conversion_factors:
            raise ValueError("Invalid from_unit: {}".format(from_unit))
        if to_unit not in self.conversion_factors:
            raise ValueError("Invalid to_unit: {}".format(to_unit))
        liters = value * self.conversion_factors[from_unit]
        result = liters * self.conversion_factors[to_unit]
        return result

    def convert_to_all(self, value, from_unit):
        from_unit = from_unit.lower().strip()
        if from_unit not in self.conversion_factors:
            raise ValueError("Invalid from_unit: {}".format(from_unit))
        liters = value * self.conversion_factors[from_unit]
        results = {}
        for unit, factor in self.conversion_factors.items():
            results[unit] = liters * factor
        return results

if __name__ == '__main__':
    converter = VolumeConverter()
    value = 1.5
    from_unit = 'liter'
    to_unit = 'gallon'
    result = converter.convert(value, from_unit, to_unit)
    print(result)

    value2 = 1000.0
    from_unit2 = 'milliliter'
    to_unit2 = 'fluid_ounce'
    result2 = converter.convert(value2, from_unit2, to_unit2)
    print(result2)

    value3 = 5.0
    from_unit3 = 'gallon'
    all_results = converter.convert_to_all(value3, from_unit3)
    print(all_results)