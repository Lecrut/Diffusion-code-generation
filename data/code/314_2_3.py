class ItemCalculator:
    def calculate_total(self, items):
        total = 0
        for item in items:
            total += item
        return total
if __name__ == '__main__':
    calculator = ItemCalculator()
    list1 = [10, 20, 30, 40]
    list2 = [5, 15, 25]
    list3 = [100, -50, 75]
    total1 = calculator.calculate_total(list1)
    print(f"Total for {list1}: {total1}")
    total2 = calculator.calculate_total(list2)
    print(f"Total for {list2}: {total2}")
    total3 = calculator.calculate_total(list3)
    print(f"Total for {list3}: {total3}")