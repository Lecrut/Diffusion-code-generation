class VolumeConverter:
    _factors_to_base = {
        'liter': 1.0,
        'milliliter': 0.001,
        'gallon_us': 3.785411784,
        'quart_us': 0.946352946,
        'pint_us': 0.473176473,
        'cup_us': 0.2365882365,
        'fluid_ounce_us': 0.0295735295625,
        'tablespoon_us': 0.01478676478125,
        'teaspoon_us': 0.00492892159375,
        'cubic_meter': 1000.0,
        'cubic_decimeter': 1.0,
        'cubic_centimeter': 0.001,
        'cubic_inch': 0.016387064,
        'cubic_foot': 28.316846592,
        'barrel_oil': 158.987294928,
    }

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        if from_unit not in cls._factors_to_base:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in cls._factors_to_base:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        if from_unit == to_unit:
            return value
        base_value = value * cls._factors_to_base[from_unit]
        return base_value / cls._factors_to_base[to_unit]

    @classmethod
    def to_base_unit(cls, value, unit):
        if unit not in cls._factors_to_base:
            raise ValueError(f"Unsupported unit: {unit}")
        return value * cls._factors_to_base[unit]

    @classmethod
    def from_base_unit(cls, value, unit):
        if unit not in cls._factors_to_base:
            raise ValueError(f"Unsupported unit: {unit}")
        return value / cls._factors_to_base[unit]

if __name__ == '__main__':
    converter = VolumeConverter()
    gallons_to_liters = converter.convert(5, 'gallon_us', 'liter')
    liters_to_quarts = converter.convert(10, 'liter', 'quart_us')
    cubic_feet_to_liters = converter.convert(100, 'cubic_foot', 'liter')
    milliliters_to_teaspoons = converter.convert(50, 'milliliter', 'teaspoon_us')
    print(f"5 gallons_us = {gallons_to_liters} liters")
    print(f"10 liters = {liters_to_quarts} quarts_us")
    print(f"100 cubic_foot = {cubic_feet_to_liters} liters")
    print(f"50 milliliters = {milliliters_to_teaspoons} teaspoons_us")
    base_val = 100
    unit = 'gallon_us'
    to_base = converter.to_base_unit(base_val, unit)
    from_base = converter.from_base_unit(base_val, unit)
    print(f"to_base_unit({base_val}, '{unit}') = {to_base}")
    print(f"from_base_unit({base_val}, '{unit}') = {from_base}")