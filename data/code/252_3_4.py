class CompareTwoSimpleQuantitiesNowProcessor:
    def __init__(self):
        self.quantity1 = None
        self.quantity2 = None

    def update_quantities(self, q1, q2):
        self.quantity1 = q1
        self.quantity2 = q2

    def get_greater_quantity(self):
        if self.quantity1 is not None and self.quantity2 is not None:
            return max(self.quantity1, self.quantity2)
        else:
            raise ValueError("Quantities are not set")

if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    processor.update_quantities(10, 20)
    print(processor.get_greater_quantity())