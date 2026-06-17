class RangeCalculator:
    def calculate_range(self, numbers):
        if not numbers:
            return 0
        minimum = numbers[0]
        maximum = numbers[0]
        for number in numbers:
            if number < minimum:
                minimum = number
            if number > maximum:
                maximum = number
        return maximum - minimum
if __name__ == '__main__':
    calculator = RangeCalculator()
    data1 = [10, 5, 20, 3, 15]
    result1 = calculator.calculate_range(data1)
    print(result1)
    data2 = [-5, 100, 0, -20]
    result2 = calculator.calculate_range(data2)
    print(result2)
    data3 = [7]
    result3 = calculator.calculate_range(data3)
    print(result3)
    data4 = []
    result4 = calculator.calculate_range(data4)
    print(result4)