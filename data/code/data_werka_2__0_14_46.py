MM_TO_KM = 1e-06
KM_TO_MM = 1000000
MM_TO_FT = 0.00328084
FT_TO_MM = 304.8
MM_TO_YD = 0.00109361
YD_TO_MM = 914.4

def convert_length(value, from_unit, to_unit):
    if from_unit == 'mm' and to_unit == 'km' or (from_unit == 'km' and to_unit == 'mm'):
        return value * MM_TO_KM if from_unit == 'mm' else value * KM_TO_MM
    elif from_unit == 'mm' and to_unit == 'ft' or (from_unit == 'ft' and to_unit == 'mm'):
        return value * MM_TO_FT if from_unit == 'mm' else value * FT_TO_MM
    elif from_unit == 'mm' and to_unit == 'yd' or (from_unit == 'yd' and to_unit == 'mm'):
        return value * MM_TO_YD if from_unit == 'mm' else value * YD_TO_MM
    else:
        raise ValueError('Unsupported unit conversion')
if __name__ == '__main__':
    print(convert_length(1000, 'mm', 'km'))
    print(convert_length(5, 'km', 'mm'))
    print(convert_length(12, 'in', 'ft'))
    print(convert_length(3, 'yd', 'cm'))