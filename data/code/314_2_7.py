class ItemCalculator:
    def calculate_total(self, items):
        total = 0
        for item in items:
            total += item
        return total
if __name__ == '__main__':
    calculator = ItemCalculator()
    sample_list1 = [10, 25, 30, 5]
    result1 = calculator.calculate_total(sample_list1)
    print(f"The total of {sample_list1} is: {result1}")
    sample_list2 = [1.5, 2.5, 3.0]
    result2 = calculator.calculate_total(sample_list2)
    print(f"The total of {sample_list2} is: {result2}")
    sample_list3 = [100]
    result3 = calculator.calculate_total(sample_list3)
    print(f"The total of {sample_list3} is: {result3}")