class StatisticsCalculator:
    def compute_average(self, numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    data1 = [10.5, 20.5, 30.0, 40.0]
    data2 = [5.0, 15.0, 25.0]
    data3 = []
    average1 = calculator.compute_average(data1)
    average2 = calculator.compute_average(data2)
    average3 = calculator.compute_average(data3)
    print(f"Average of {data1}: {average1}")
    print(f"Average of {data2}: {average2}")
    print(f"Average of {data3}: {average3}")