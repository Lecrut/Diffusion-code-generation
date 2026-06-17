class ItemCalculator:
    def calculate_total(self, items):
        total = 0
        for item in items:
            total += item
        return total
if __name__ == '__main__':
    calculator = ItemCalculator()
    list1 = [10, 25, 30, 5]
    list2 = [1.5, 2.5, 3.0]
    list3 = [-10, 5, 15]
    total1 = calculator.calculate_total(list1)
    print(f"The total of {list1} is: {total1}")
    total2 = calculator.calculate_total(list2)
    print(f"The total of {list2} is: {total2}")
    total3 = calculator.calculate_total(list3)
    print(f"The total of {list3} is: {total3}")