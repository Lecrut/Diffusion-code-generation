class LengthConverter:
    METER_TO_FOOT = 3.28084
    FOOT_TO_METER = 1 / METER_TO_FOOT

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'meter' and to_unit == 'foot':
            return value * self.METER_TO_FOOT
        if from_unit == 'foot' and to_unit == 'meter':
            return value * self.FOOT_TO_METER
        if from_unit == 'foot' and to_unit == 'meter':
            return value * self.FOOT_TO_METER
        if from_unit == 'meter' and to_unit == 'foot':
            return value * self.METER_TO_FOOT
        if from_unit == 'meter' and to_unit == 'meter':
            return value
        if from_unit == 'foot' and to_unit == 'foot':
            return value
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'meter', 'foot'))
    print(converter.convert(32.8084, 'foot', 'meter'))
    print(converter.convert(5, 'meter', 'meter'))
    print(converter.convert(100, 'foot', 'foot'))