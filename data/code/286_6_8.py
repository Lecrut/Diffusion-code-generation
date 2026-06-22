class LengthConverter:
    def __init__(self, value=0, unit='inches'):
        self.value = value
        self.unit = unit

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def convert_to_cm(self):
        if self.unit == 'inches':
            return self.value * 2.54
        elif self.unit == 'cm':
            return self.value
        else:
            raise ValueError("Unsupported unit")

    def convert_to_inches(self):
        if self.unit == 'inches':
            return self.value
        elif self.unit == 'cm':
            return self.value / 2.54
        else:
            raise ValueError("Unsupported unit")

if __name__ == '__main__':
    converter = LengthConverter(10, 'inches')
    print(f"Value in inches: {converter.get_value()}")
    print(f"Value in cm: {converter.convert_to_cm()}")
    converter.set_value(25)
    converter.unit = 'cm'
    print(f"Value in inches: {converter.convert_to_inches()}")