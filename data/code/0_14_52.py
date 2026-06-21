MM_TO_KM = 1e-06
KM_TO_MM = 1000000.0
MM_TO_FT = 0.00328084
FT_TO_MM = 304.8
MM_TO_YD = 0.00109361
YD_TO_MM = 914.4

def convert_length(value, from_unit, to_unit):

    def mm_to_km(v):
        return v * MM_TO_KM

    def km_to_mm(v):
        return v * KM_TO_MM

    def mm_to_ft(v):
        return v * MM_TO_FT

    def ft_to_mm(v):
        return v * FT_TO_MM

    def mm_to_yd(v):
        return v * MM_TO_YD

    def yd_to_mm(v):
        return v * YD_TO_MM
    conversions = {('mm', 'km'): mm_to_km, ('km', 'mm'): km_to_mm, ('mm', 'ft'): mm_to_ft, ('ft', 'mm'): ft_to_mm, ('mm', 'yd'): mm_to_yd, ('yd', 'mm'): yd_to_mm}
    if (from_unit, to_unit) not in conversions:
        raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
    return conversions[from_unit, to_unit](value)
if __name__ == '__main__':
    print(convert_length(1000, 'mm', 'km'))
    print(convert_length(5, 'km', 'mm'))
    print(convert_length(200, 'mm', 'yd'))
    print(convert_length(10, 'yd', 'ft'))