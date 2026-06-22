class YardConverter:
    CONVERSION_FACTOR = 0.9144

    @staticmethod
    def validate_yards(yards):
        if not all(isinstance(y, (int, float)) and y >= 0 for y in yards):
            raise ValueError("All yard values must be non-negative numbers")

    def convert(self, yards):
        self.validate_yards(yards)
        return [round(y * self.CONVERSION_FACTOR, 3) for y in yards]

if __name__ == '__main__':
    converter = YardConverter()
    sample_yards = [10, 20, 30]
    print(converter.convert(sample_yards))