class MassConverter:
    def tons_to_kilograms(self, tons):
        return round(tons * 907.184, 2)

if __name__ == '__main__':
    converter = MassConverter()
    sample_tons = [1.5, 10.25, 500.75, 0.001]
    for tons in sample_tons:
        print(converter.tons_to_kilograms(tons))