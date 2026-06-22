class DistanceConverter:

    def __init__(self):
        self.inch_to_mm = 25.4

    def to_millimeters(self, value, unit):
        if unit == 'in':
            return value * self.inch_to_mm
        else:
            raise ValueError("Invalid unit. Use 'in'.")
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.to_millimeters(1, 'in'))
    print(converter.to_millimeters(10, 'in'))