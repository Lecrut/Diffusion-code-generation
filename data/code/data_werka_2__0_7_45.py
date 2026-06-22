class LengthConverter:
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 1 / METERS_TO_FEET

    def convert(self, value, from_unit, to_unit):
        if (from_unit == 'm' and to_unit == 'ft'):
            return value * self.METERS_TO_FEET
        elif (from_unit == 'ft' and to_unit == 'm'):
            return value * self.FEET_TO_METERS
        else:
            raise ValueError('Unsupported unit conversion')

if __name__ == '__main__':
    converter = LengthConverter()
    sample_value_meters = 10.0
    sample_value_feet = 32.8084

    try:
        converted_to_feet = converter.convert(sample_value_meters, 'm', 'ft')
        print(f"{sample_value_meters} meters is {converted_to_feet:.6f} feet")

        converted_to_meters = converter.convert(sample_value_feet, 'ft', 'm')
        print(f"{sample_value_feet} feet is {converted_to_meters:.6f} meters")
    except ValueError as e:
        print(e)