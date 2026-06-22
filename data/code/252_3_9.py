class CompareTwoSimpleQuantitiesNowProcessor:
    MIN_VALUE = 0
    MAX_VALUE = 100

    @staticmethod
    def validate(value):
        if not (CompareTwoSimpleQuantitiesNowProcessor.MIN_VALUE <= value <= CompareTwoSimpleQuantitiesNowProcessor.MAX_VALUE):
            raise ValueError(f"Value must be between {CompareTwoSimpleQuantitiesNowProcessor.MIN_VALUE} and {CompareTwoSimpleQuantitiesNowProcessor.MAX_VALUE}")

    def __init__(self):
        self.data = {}

    def update_data(self, key, value):
        CompareTwoSimpleQuantitiesNowProcessor.validate(value)
        self.data[key] = value

    def get_computed_result(self, key1, key2):
        if key1 in self.data and key2 in self.data:
            return self.data[key1] + self.data[key2]
        else:
            raise ValueError("One or both keys not found in data")

if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    processor.update_data('quantity1', 50)
    processor.update_data('quantity2', 30)
    print(processor.get_computed_result('quantity1', 'quantity2'))