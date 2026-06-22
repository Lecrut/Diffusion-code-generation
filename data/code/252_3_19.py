class CompareTwoSimpleQuantitiesNowProcessor:
    def __init__(self):
        self.data = {
            'quantity1': 0,
            'quantity2': 0,
            'result': None
        }

    def update_quantities(self, quantity1, quantity2):
        self.data['quantity1'] = quantity1
        self.data['quantity2'] = quantity2

    def compute_result(self):
        if self.data['quantity1'] > self.data['quantity2']:
            self.data['result'] = 'Greater'
        elif self.data['quantity1'] < self.data['quantity2']:
            self.data['result'] = 'Less'
        else:
            self.data['result'] = 'Equal'

    def get_result(self):
        return self.data['result']

if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    processor.update_quantities(10, 5)
    processor.compute_result()
    print(processor.get_result())