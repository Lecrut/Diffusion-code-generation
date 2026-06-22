class CompareTwoSimpleQuantitiesNowProcessor:
    DEFAULT_DATA = {
        'quantity1': 0,
        'quantity2': 0
    }

    @staticmethod
    def compare_values(value1, value2):
        if value1 > value2:
            return f"{value1} is greater than {value2}"
        elif value1 < value2:
            return f"{value1} is less than {value2}"
        else:
            return f"{value1} is equal to {value2}"

    def __init__(self):
        self.data = self.DEFAULT_DATA.copy()

    def update_data(self, key, value):
        if key in self.data:
            self.data[key] = value

    def get_computed_result(self, key1, key2):
        if key1 in self.data and key2 in self.data:
            return CompareTwoSimpleQuantitiesNowProcessor.compare_values(self.data[key1], self.data[key2])
        else:
            raise ValueError("One or both keys not found in data")

if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    processor.update_data('quantity1', 5)
    processor.update_data('quantity2', 3)
    print(processor.get_computed_result('quantity1', 'quantity2'))