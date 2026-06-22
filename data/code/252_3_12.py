class CompareTwoSimpleQuantitiesNowProcessor:
    def __init__(self):
        self.quantity1 = None
        self.quantity2 = None

    def update_quantities(self, q1, q2):
        self.quantity1 = q1
        self.quantity2 = q2

    def get_comparison_result(self):
        if self.quantity1 is None or self.quantity2 is None:
            return "Quantities not set"
        elif self.quantity1 > self.quantity2:
            return f"{self.quantity1} is greater than {self.quantity2}"
        elif self.quantity1 < self.quantity2:
            return f"{self.quantity1} is less than {self.quantity2}"
        else:
            return f"{self.quantity1} is equal to {self.quantity2}"

if __name__ == '__main__':
    processor = CompareTwoSimpleQuantitiesNowProcessor()
    processor.update_quantities(5, 3)
    print(processor.get_comparison_result())