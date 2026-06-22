class LengthConverter:

    def __init__(self):
        self.conversion_factor = 0.3048

    def feet_to_meters(self, feet):
        try:
            return feet * self.conversion_factor
        except TypeError:
            return None
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.feet_to_meters(1))
    print(converter.feet_to_meters(5))
    print(converter.feet_to_meters('a'))