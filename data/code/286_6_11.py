class LengthConverter:
    INCHES_TO_CM = 2.54
    CM_TO_INCHES = 1 / INCHES_TO_CM

    @staticmethod
    def convert_to_cm(value, unit):
        if unit == 'in':
            return value * LengthConverter.INCHES_TO_CM
        elif unit == 'cm':
            return value
        else:
            raise ValueError(f'Unknown unit: {unit}')

    @staticmethod
    def convert_from_cm(value, unit):
        if unit == 'in':
            return value * LengthConverter.CM_TO_INCHES
        elif unit == 'cm':
            return value
        else:
            raise ValueError(f'Unknown unit: {unit}')
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert_to_cm(10, 'in'))
    print(converter.convert_from_cm(25.4, 'cm'))