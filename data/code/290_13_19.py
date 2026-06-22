class MassConverter:
    CONVERSION_FACTOR = 907.184

    @staticmethod
    def tons_to_kilograms(tons):
        return round(tons * MassConverter.CONVERSION_FACTOR, 2)

if __name__ == '__main__':
    sample_tons = [1.5, 10.25, 500.75, 0.001]
    for tons in sample_tons:
        print(MassConverter.tons_to_kilograms(tons))