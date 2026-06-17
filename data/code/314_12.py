class ItemCalculator:
    def __init__(self):
        self._items = []
    def add_items(self, items):
        self._items.extend(items)
    def calculate_total_sum(self):
        return sum(self._items)
if __name__ == '__main__':
    calculator = ItemCalculator()
    sample_data1 = [10, 20, 30, 40]
    calculator.add_items(sample_data1)
    total1 = calculator.calculate_total_sum()
    print(f"Total sum for sample data 1: {total1}")
    calculator2 = ItemCalculator()
    sample_data2 = [5, 15, 25]
    calculator2.add_items(sample_data2)
    total2 = calculator2.calculate_total_sum()
    print(f"Total sum for sample data 2: {total2}")