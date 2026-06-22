class CompareTwoSimpleQuantitiesNowProcessor:
    def __init__(self):
        self.data = {}

    def update_data(self, key, value):
        if isinstance(value, (int, float)):
            self.data[key] = value
        else:
            raise ValueError("Value must be an integer or a float")

    def get_computed_result(self, key1, key2):
        if key1 in self.data and key2 in self.data:
            return {
                'sum': self.data[key1] + self.data[key2],
                'difference': abs(self.data[key1] - self.data[key2])
            }
        else:
            raise ValueError("One or both keys not found in data")

if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    processor.update_data('quantity1', 5)
    processor.update_data('quantity2', 3)
    result = processor.get_computed_result('quantity1', 'quantity2')
    print(f"Sum: {result['sum']}, Difference: {result['difference']}")