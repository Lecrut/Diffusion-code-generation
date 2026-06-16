class SequenceCalculator:
    def calculate_sum(self, numbers):
        total = 0
        for number in numbers:
            total += number
        return total
if __name__ == '__main__':
    calculator = SequenceCalculator()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [-1, 5, 10]
    print(calculator.calculate_sum(list1))
    print(calculator.calculate_sum(list2))
    print(calculator.calculate_sum(list3))