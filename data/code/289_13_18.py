class YardConverter:
    CONVERSION_FACTOR = 0.9144

    @staticmethod
    def yards_to_meters(yards):
        return [round(y * YardConverter.CONVERSION_FACTOR, 3) for y in yards]

if __name__ == '__main__':
    converter = YardConverter()
    sample_yards = [10, 20, 30]
    print(converter.yards_to_meters(sample_yards))