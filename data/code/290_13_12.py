class MassConverter:
    TONS_TO_KILOGRAMS_FACTOR = 907.184

    @staticmethod
    def tons_to_kilograms(tons):
        return round(tons * MassConverter.TONS_TO_KILOGRAMS_FACTOR, 2)

if __name__ == '__main__':
    converter = MassConverter()
    sample_tons = [2.5, 3.75, 0.1, 10.0]
    for tons in sample_tons:
        print(converter.tons_to_kilograms(tons))