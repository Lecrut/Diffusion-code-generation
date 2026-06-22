class CompareTwoSimpleQuantitiesNowProcessor:
    def __init__(self):
        self.data = {
            'quantity1': None,
            'quantity2': None,
            'result': None
        }

    def update_quantities(self, quantity1, quantity2):
        self.data['quantity1'] = quantity1
        self.data['quantity2'] = quantity2

    def compute_result(self):
        if self.data['quantity1'] is not None and self.data['quantity2'] is not None:
            self.data['result'] = self.data['quantity1'] + self.data['quantity2']
        else:
            raise ValueError("Both quantities must be set to compute the result")

    def get_result(self):
        return self.data['result']

if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    processor.update_quantities(5, 3)
    processor.compute_result()
    print(processor.get_result())