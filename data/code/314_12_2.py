class ItemCalculator:
    def __init__(self, items):
        self._items = items
    def calculate_total(self):
        total = 0
        for item in self._items:
            total += item
        return total
if __name__ == '__main__':
    sample_data = [10, 25, 5, 40]
    calculator = ItemCalculator(sample_data)
    result = calculator.calculate_total()
    print(result)