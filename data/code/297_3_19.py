class WeightConverter:

    def __init__(self):
        self.conversion_factor = 0.453592

    def pounds_to_kilograms(self, pounds):
        return pounds * self.conversion_factor
if __name__ == '__main__':
    converter = WeightConverter()
    print(converter.pounds_to_kilograms(1))
    print(converter.pounds_to_kilograms(2.5))