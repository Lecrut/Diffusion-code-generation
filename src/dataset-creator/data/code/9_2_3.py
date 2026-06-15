class StatisticsCalculator:
    def compute_average(self, numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    data1 = [10.5, 20.5, 30.0, 40.0]
    data2 = [1.1, 2.2, 3.3, 4.4, 5.5]
    data3 = []
    avg1 = calculator.compute_average(data1)
    avg2 = calculator.compute_average(data2)
    avg3 = calculator.compute_average(data3)
    print(f"Average of {data1}: {avg1}")
    print(f"Average of {data2}: {avg2}")
    print(f"Average of {data3}: {avg3}")