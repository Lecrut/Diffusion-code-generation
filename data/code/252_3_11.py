class CompareTwoSimpleQuantitiesNowProcessor:
    def __init__(self):
        self.data = {}

    def update_data(self, key, value):
        self.data[key] = value

    def get_computed_result(self, key1, key2):
        if key1 in self.data and key2 in self.data:
            return self.data[key1] * self.data[key2]
        else:
            raise ValueError("One or both keys not found in data")

if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    processor.update_data('quantity1', 5)
    processor.update_data('quantity2', 3)
    print(processor.get_computed_result('quantity1', 'quantity2'))