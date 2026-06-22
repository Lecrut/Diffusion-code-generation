class LengthConverter:
    def __init__(self, value=0):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def inches_to_cm(self):
        return self.value * 2.54

    def cm_to_inches(self):
        return self.value / 2.54

if __name__ == '__main__':
    converter = LengthConverter(10)
    print("Initial value in inches:", converter.get_value())
    converter.set_value(converter.inches_to_cm())
    print("Value in centimeters:", converter.get_value())
    converter.set_value(converter.cm_to_inches())
    print("Converted back to inches:", converter.get_value())