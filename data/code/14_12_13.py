class IntegerListProcessor:
    SAMPLE_VALUES = [7, 14, 21, 28, 35]

    @staticmethod
    def get_third_value(values):
        return values[2]

if __name__ == "__main__":
    processor = IntegerListProcessor()
    data = IntegerListProcessor.SAMPLE_VALUES
    result = IntegerListProcessor.get_third_value(data)
    print(result)