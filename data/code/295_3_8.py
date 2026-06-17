def convert_to_base(value, unit):
    conversions = {
        'length': {
            'meter': 1.0,
            'kilometer': 1000.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'inch': 0.0254,
            'foot': 0.3048,
            'mile': 1609.34
        },
        'mass': {
            'kilogram': 1.0,
            'gram': 0.001,
            'milligram': 0.000001,
            'pound': 0.453592,
            'ounce': 0.0283495
        },
        'volume': {
            'liter': 1.0,
            'milliliter': 0.001,
            'cubic_meter': 1.0,
            'cubic_centimeter': 0.000001
        }
    }
    if unit in conversions:
        base_unit = None
        factor = 1.0
        if unit == 'length':
            for base, fact in conversions['length'].items():
                if fact != 1.0:
                    if value > 0 and (value / fact) == round(value / fact):
                        base_unit = base
                        factor = fact
                        break
            if base_unit:
                return value / factor
        elif unit == 'mass':
            for base, fact in conversions['mass'].items():
                if fact != 1.0:
                    if value > 0 and (value / fact) == round(value / fact):
                        base_unit = base
                        factor = fact
                        break
            if base_unit:
                return value / factor
        elif unit == 'volume':
            for base, fact in conversions['volume'].items():
                if fact != 1.0:
                    if value > 0 and (value / fact) == round(value / fact):
                        base_unit = base
                        factor = fact
                        break
            if base_unit:
                return value / factor
        else:
            return value
    return value
if __name__ == '__main__':
    print("--- Length Conversions ---")
    print("1000 meters to meters:", convert_to_base(1000, 'kilometer'))
    print("2.54 meters to meters:", convert_to_base(2.54, 'inch'))
    print("10 feet to meters:", convert_to_base(10, 'foot'))
    print("500 centimeters to meters:", convert_to_base(500, 'centimeter'))
    print("\n--- Mass Conversions ---")
    print("2 kilograms to kilograms:", convert_to_base(2, 'gram'))
    print("1 pound to kilogram:", convert_to_base(1, 'pound'))
    print("1000 grams to kilograms:", convert_to_base(1000, 'gram'))
    print("\n--- Volume Conversions ---")
    print("1 liter to liters:", convert_to_base(1, 'milliliter'))
    print("5 cubic meters to cubic meters:", convert_to_base(5, 'cubic_meter'))
    print("2000 milliliters to liters:", convert_to_base(2000, 'milliliter'))
    print("\n--- Unknown Unit Test ---")
    print("100 unknown unit:", convert_to_base(100, 'lightyear'))