class LengthConverter:
    M_TO_KM = 0.001
    M_TO_CM = 100
    M_TO_MM = 1000
    M_TO_IN = 39.3701
    M_TO_FT = 3.28084
    M_TO_YD = 1.09361
    M_TO_MI = 0.000621371
    KM_TO_M = 1 / M_TO_KM
    CM_TO_M = 1 / M_TO_CM
    MM_TO_M = 1 / M_TO_MM
    IN_TO_M = 1 / M_TO_IN
    FT_TO_M = 1 / M_TO_FT
    YD_TO_M = 1 / M_TO_YD
    MI_TO_M = 1 / M_TO_MI

    @staticmethod
    def convert(value, from_unit, to_unit):
        conversion_factors = {('m', 'km'): LengthConverter.M_TO_KM, ('m', 'cm'): LengthConverter.M_TO_CM, ('m', 'mm'): LengthConverter.M_TO_MM, ('m', 'in'): LengthConverter.M_TO_IN, ('m', 'ft'): LengthConverter.M_TO_FT, ('m', 'yd'): LengthConverter.M_TO_YD, ('m', 'mi'): LengthConverter.M_TO_MI, ('km', 'm'): LengthConverter.KM_TO_M, ('cm', 'm'): LengthConverter.CM_TO_M, ('mm', 'm'): LengthConverter.MM_TO_M, ('in', 'm'): LengthConverter.IN_TO_M, ('ft', 'm'): LengthConverter.FT_TO_M, ('yd', 'm'): LengthConverter.YD_TO_M, ('mi', 'm'): LengthConverter.MI_TO_M, ('km', 'cm'): LengthConverter.KM_TO_M * LengthConverter.M_TO_CM, ('km', 'mm'): LengthConverter.KM_TO_M * LengthConverter.M_TO_MM}
        key = (from_unit, to_unit)
        if key in conversion_factors:
            return value * conversion_factors[key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'm', 'km'))
    print(converter.convert(100, 'cm', 'm'))
    print(converter.convert(500, 'mm', 'in'))
    print(converter.convert(2, 'yd', 'ft'))
    print(converter.convert(1, 'mi', 'km'))