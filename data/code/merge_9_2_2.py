class StatisticsCalculator:
    def compute_average(self, numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    data1 = [10.5, 20.5, 30.0, 40.0]
    data2 = [1.5, 2.5, 3.5]
    data3 = []
    data4 = [7.0]
    avg1 = calculator.compute_average(data1)
    avg2 = calculator.compute_average(data2)
    avg3 = calculator.compute_average(data3)
    avg4 = calculator.compute_average(data4)
    print(f"Average of {data1}: {avg1}")
    print(f"Average of {data2}: {avg2}")
    print(f"Average of {data3}: {avg3}")
    print(f"Average of {data4}: {avg4}")