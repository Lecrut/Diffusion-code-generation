class CompareTwoSimpleQuantitiesNowProcessor:

    def __init__(self):
        self.quantity_a = None
        self.quantity_b = None

    def update_quantities(self, a, b):
        self.quantity_a = a
        self.quantity_b = b

    def get_greater_quantity(self):
        if self.quantity_a > self.quantity_b:
            return self.quantity_a
        elif self.quantity_b > self.quantity_a:
            return self.quantity_b
        else:
            return None
if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    processor.update_quantities(10, 20)
    print(processor.get_greater_quantity())