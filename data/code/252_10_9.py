class QuantityComparator:
    def __init__(self):
        self.quantity1 = 0
        self.quantity2 = 0

    def set_quantities(self, quantity1, quantity2):
        self.quantity1 = quantity1
        self.quantity2 = quantity2

    def compare_two_simple_quantities_now_calculate(self):
        if not isinstance(self.quantity1, (int, float)) or not isinstance(self.quantity2, (int, float)):
            raise ValueError("Both inputs must be numbers")
        if self.quantity1 > self.quantity2:
            return 'Quantity 1 is greater'
        elif self.quantity1 < self.quantity2:
            return 'Quantity 2 is greater'
        else:
            return 'Quantities are equal'

if __name__ == '__main__':
    comparator = QuantityComparator()
    comparator.set_quantities(10, 20)
    result = comparator.compare_two_simple_quantities_now_calculate()
    print(result)