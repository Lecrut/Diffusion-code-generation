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
    list3 = [-1, 5, -3, 10]
    sum1 = calculator.calculate_sum(list1)
    print(f"The sum of {list1} is: {sum1}")
    sum2 = calculator.calculate_sum(list2)
    print(f"The sum of {list2} is: {sum2}")
    sum3 = calculator.calculate_sum(list3)
    print(f"The sum of {list3} is: {sum3}")