class AverageCalculator:
    def calculate_average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    data1 = [10, 20, 30, 40, 50]
    average1 = calculator.calculate_average(data1)
    print(f"The average of {data1} is: {average1}")
    data2 = [5, 15, 25]
    average2 = calculator.calculate_average(data2)
    print(f"The average of {data2} is: {average2}")
    data3 = []
    average3 = calculator.calculate_average(data3)
    print(f"The average of {data3} is: {average3}")