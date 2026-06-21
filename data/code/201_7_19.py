class AverageCalculator:
    def calculate(self, numbers):
        return sum(numbers) / len(numbers) if numbers else 0

if __name__ == '__main__':
    calc = AverageCalculator()
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15, 25]
    data3 = []
    print(f"Average of {data1}: {calc.calculate(data1)}")
    print(f"Average of {data2}: {calc.calculate(data2)}")
    print(f"Average of {data3}: {calc.calculate(data3)}")