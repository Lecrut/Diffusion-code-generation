class PenultimateExtractor:
    MIN_LENGTH = 2
    EXPECTED_TYPE = list

    @staticmethod
    def validate_sequence(data):
        if not isinstance(data, PenultimateExtractor.EXPECTED_TYPE):
            raise TypeError("Input must be a list")
        if len(data) < PenultimateExtractor.MIN_LENGTH:
            raise ValueError("List must contain at least two elements")

    @classmethod
    def extract(cls, data):
        cls.validate_sequence(data)
        return data[-2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = PenultimateExtractor.extract(sample_data)
    print(result)