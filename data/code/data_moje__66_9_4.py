class KilometerConverter:
    FACTOR = 1000

    def __init__(self, source_tuple):
        self.source_tuple = source_tuple

    def convert(self):
        return tuple(map(self.scale_value, self.source_tuple))

    def scale_value(self, value):
        return value * self.FACTOR

if __name__ == '__main__':
    data = (0.1, 1.5, 42, 99.99)
    converter_instance = KilometerConverter(data)
    print(converter_instance.convert())