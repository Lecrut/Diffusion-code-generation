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

    CONVERSION_FACTORS = {
        'm_to_km': M_TO_KM,
        'm_to_cm': M_TO_CM,
        'm_to_mm': M_TO_MM,
        'm_to_in': M_TO_IN,
        'm_to_ft': M_TO_FT,
        'm_to_yd': M_TO_YD,
        'm_to_mi': M_TO_MI,
        'km_to_m': KM_TO_M,
        'cm_to_m': CM_TO_M,
        'mm_to_m': MM_TO_M,
        'in_to_m': IN_TO_M,
        'ft_to_m': FT_TO_M,
        'yd_to_m': YD_TO_M,
        'mi_to_m': MI_TO_M
    }

    @staticmethod
    def convert(value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in LengthConverter.CONVERSION_FACTORS:
            return value * LengthConverter.CONVERSION_FACTORS[key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'm', 'km'))
    print(converter.convert(100, 'cm', 'm'))
    print(converter.convert(500, 'mm', 'in'))
    print(converter.convert(2, 'yd', 'ft'))
    print(converter.convert(1, 'mi', 'km'))