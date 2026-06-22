class LengthConverter:
    MM_TO_KM = 1e-06
    KM_TO_MM = 1000000
    MM_TO_FT = 0.00328084
    FT_TO_MM = 304.8
    MM_TO_YD = 0.00109361
    YD_TO_MM = 914.4

    @staticmethod
    def convert(value, from_unit, to_unit):
        conversion_map = {('mm', 'km'): LengthConverter.MM_TO_KM, ('km', 'mm'): LengthConverter.KM_TO_MM, ('mm', 'ft'): LengthConverter.MM_TO_FT, ('ft', 'mm'): LengthConverter.FT_TO_MM, ('mm', 'yd'): LengthConverter.MM_TO_YD, ('yd', 'mm'): LengthConverter.YD_TO_MM}
        conversion_key = (from_unit, to_unit)
        if conversion_key not in conversion_map:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
        return value * conversion_map[conversion_key]
if __name__ == '__main__':
    print(LengthConverter.convert(1000, 'mm', 'km'))
    print(LengthConverter.convert(5, 'km', 'mm'))
    print(LengthConverter.convert(200, 'mm', 'yd'))
    print(LengthConverter.convert(10, 'yd', 'mm'))