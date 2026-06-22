class UnitConverter:
    KG_TO_LB = 2.20462
    LB_TO_KG = 1 / 2.20462
    KG_TO_OZ = 35.274
    OZ_TO_KG = 1 / 35.274

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == 'kg' and to_unit == 'lb':
            return value * UnitConverter.KG_TO_LB
        elif from_unit == 'lb' and to_unit == 'kg':
            return value * UnitConverter.LB_TO_KG
        elif from_unit == 'kg' and to_unit == 'oz':
            return value * UnitConverter.KG_TO_OZ
        elif from_unit == 'oz' and to_unit == 'kg':
            return value * UnitConverter.OZ_TO_KG
        else:
            raise ValueError('Unsupported conversion')
if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.convert(1, 'kg', 'lb'))
    print(converter.convert(2.20462, 'lb', 'kg'))
    print(converter.convert(1, 'kg', 'oz'))
    print(converter.convert(35.274, 'oz', 'kg'))