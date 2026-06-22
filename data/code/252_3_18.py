class CompareTwoSimpleQuantitiesNowProcessor:
    def __init__(self):
        self.sample_data = {
            'quantity1': 10,
            'quantity2': 20
        }
    
    def update_quantity(self, quantity_name, new_value):
        if quantity_name in self.sample_data:
            self.sample_data[quantity_name] = new_value
    
    def get_computed_result(self):
        return self.sample_data['quantity1'] + self.sample_data['quantity2']

if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    print(processor.get_computed_result())
    processor.update_quantity('quantity1', 30)
    print(processor.get_computed_result())