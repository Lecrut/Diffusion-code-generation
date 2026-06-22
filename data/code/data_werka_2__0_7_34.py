class LengthConverter:
    M_TO_Ft = 3.28084
    Ft_TO_M = 1 / M_TO_Ft

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == 'm' and to_unit == 'ft':
            return value * LengthConverter.M_TO_Ft
        elif from_unit == 'ft' and to_unit == 'm':
            return value * LengthConverter.Ft_TO_M
        else:
            raise ValueError('Unsupported unit conversion')

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(5, 'm', 'ft'))
    print(converter.convert(16.4042, 'ft', 'm'))