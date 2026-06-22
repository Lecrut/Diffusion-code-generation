class CompareTwoSimpleQuantitiesNowProcessor:

    def __init__(self):
        self.data = {'quantity1': None, 'quantity2': None, 'result': None}

    def update_quantity1(self, value):
        self.data['quantity1'] = value

    def update_quantity2(self, value):
        self.data['quantity2'] = value

    def compute_result(self):
        if self.data['quantity1'] is not None and self.data['quantity2'] is not None:
            self.data['result'] = self.data['quantity1'] + self.data['quantity2']
        else:
            self.data['result'] = None
        return self.data['result']
if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    processor.update_quantity1(5)
    processor.update_quantity2(3)
    print(processor.compute_result())