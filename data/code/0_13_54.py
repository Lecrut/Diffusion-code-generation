class LengthConverter:
    M_TO_CM = 100
    CM_TO_M = 0.01
    M_TO_IN = 39.3701
    IN_TO_M = 0.0254
    CM_TO_IN = 0.393701
    IN_TO_CM = 2.54

    @staticmethod
    def convert(value, from_unit, to_unit):
        conversion_key = f'{from_unit}_to_{to_unit}'
        if hasattr(LengthConverter, conversion_key):
            return value * getattr(LengthConverter, conversion_key)
        else:
            raise ValueError('Unsupported unit conversion')

if __name__ == '__main__':
    sample_values = [
        (1, 'm', 'cm'),
        (2.54, 'cm', 'in'),
        (10, 'in', 'm')
    ]
    for value, from_unit, to_unit in sample_values:
        converted_value = LengthConverter.convert(value, from_unit, to_unit)
        print(f"{value} {from_unit} is {converted_value} {to_unit}")