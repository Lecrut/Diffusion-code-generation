class MassConverter:
    def __init__(self):
        self.conversion_factor = 907.184

    def tons_to_kilograms(self, tons):
        return round(tons * self.conversion_factor, 2)

if __name__ == '__main__':
    converter = MassConverter()
    sample_tons = [2.5, 3.75, 0.1, 10.0]
    for tons in sample_tons:
        print(converter.tons_to_kilograms(tons))