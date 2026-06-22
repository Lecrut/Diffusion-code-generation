class LengthConverter:
    M_TO_FT = 3.28084
    FT_TO_M = 1 / M_TO_FT

    @staticmethod
    def convert_length(value, unit):
        if unit == 'm':
            return value * LengthConverter.M_TO_FT
        elif unit == 'ft':
            return value * LengthConverter.FT_TO_M
        else:
            raise ValueError('Unsupported unit type')

if __name__ == '__main__':
    length_in_meters = 10
    length_in_feet = LengthConverter.convert_length(length_in_meters, 'm')
    print(f'{length_in_meters} meters is {length_in_feet:.4f} feet')
    length_in_feet = 32.8084
    length_in_meters = LengthConverter.convert_length(length_in_feet, 'ft')
    print(f'{length_in_feet} feet is {length_in_meters:.4f} meters')