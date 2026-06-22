class LengthConverter:
    M_TO_KM = 0.001
    M_TO_CM = 100
    M_TO_MM = 1000
    M_TO_IN = 39.3701
    M_TO_FT = 3.28084
    M_TO_YD = 1.09361
    M_TO_MI = 0.000621371
    KM_TO_M = 1000
    CM_TO_M = 0.01
    MM_TO_M = 0.001
    IN_TO_M = 0.0254
    FT_TO_M = 0.3048
    YD_TO_M = 0.9144
    MI_TO_M = 1609.34

    def __init__(self):
        self.conversion_factors = {'m_to_km': self.M_TO_KM, 'm_to_cm': self.M_TO_CM, 'm_to_mm': self.M_TO_MM, 'm_to_in': self.M_TO_IN, 'm_to_ft': self.M_TO_FT, 'm_to_yd': self.M_TO_YD, 'm_to_mi': self.M_TO_MI, 'km_to_m': self.KM_TO_M, 'cm_to_m': self.CM_TO_M, 'mm_to_m': self.MM_TO_M, 'in_to_m': self.IN_TO_M, 'ft_to_m': self.FT_TO_M, 'yd_to_m': self.YD_TO_M, 'mi_to_m': self.MI_TO_M}

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'm', 'km'))
    print(converter.convert(100, 'cm', 'm'))
    print(converter.convert(500, 'mm', 'in'))
    print(converter.convert(2, 'yd', 'ft'))
    print(converter.convert(1, 'mi', 'km'))