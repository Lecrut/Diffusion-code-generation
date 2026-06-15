class Calculator:
    def calculate_average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    calc = Calculator()
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15, 25]
    data3 = []
    print(f"Average of {data1}: {calc.calculate_average(data1)}")
    print(f"Average of {data2}: {calc.calculate_average(data2)}")
    print(f"Average of {data3}: {calc.calculate_average(data3)}")