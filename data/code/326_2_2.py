class StatisticsCalculator:
    def compute_average(self, numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    data1 = [10.5, 20.5, 30.0, 40.0]
    result1 = calculator.compute_average(data1)
    print(f"Average of {data1}: {result1}")
    data2 = [1.1, 2.2, 3.3, 4.4]
    result2 = calculator.compute_average(data2)
    print(f"Average of {data2}: {result2}")
    data3 = [5.0]
    result3 = calculator.compute_average(data3)
    print(f"Average of {data3}: {result3}")
    data4 = []
    result4 = calculator.compute_average(data4)
    print(f"Average of {data4}: {result4}")