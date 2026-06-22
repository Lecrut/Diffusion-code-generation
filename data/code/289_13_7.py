class YardConverter:
    CONVERSION_FACTOR = 0.9144

    @staticmethod
    def validate_yards(yards):
        if not all(isinstance(y, (int, float)) and y >= 0 for y in yards):
            raise ValueError("All yard values must be non-negative numbers")

    def yards_to_meters(self, yards):
        self.validate_yards(yards)
        return [round(y * YardConverter.CONVERSION_FACTOR, 3) for y in yards]

if __name__ == '__main__':
    converter = YardConverter()
    sample_yards = [10, 20, 30]
    print(converter.yards_to_meters(sample_yards))