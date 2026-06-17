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
    data1 = [1, 5, 2, 8, 3]
    result1 = calculator.calculate_range(data1)
    print(result1)
    data2 = [100, 50, 200, 10]
    result2 = calculator.calculate_range(data2)
    print(result2)
    data3 = []
    result3 = calculator.calculate_range(data3)
    print(result3)
    data4 = [7]
    result4 = calculator.calculate_range(data4)
    print(result4)