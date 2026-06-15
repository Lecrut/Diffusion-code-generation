class SumCalculator:
    def calculate_sum(self, numbers):
        total = 0
        for number in numbers:
            total += number
        return total
if __name__ == '__main__':
    calculator = SumCalculator()
    list1 = [1, 2, 3, 4, 5]
    tuple2 = (10, 20, 30)
    list3 = [-1, 5, 10]
    sum1 = calculator.calculate_sum(list1)
    sum2 = calculator.calculate_sum(tuple2)
    sum3 = calculator.calculate_sum(list3)
    print(f"Sum of {list1}: {sum1}")
    print(f"Sum of {tuple2}: {sum2}")
    print(f"Sum of {list3}: {sum3}")