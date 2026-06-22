class MassConverter:
    conversion_factor = 907.184

    @staticmethod
    def tons_to_kilograms(tons):
        return round(tons * MassConverter.conversion_factor, 2)

if __name__ == '__main__':
    converter = MassConverter()
    sample_tons = [1.5, 10.25, 500.75, 0.001]
    for tons in sample_tons:
        print(converter.tons_to_kilograms(tons))