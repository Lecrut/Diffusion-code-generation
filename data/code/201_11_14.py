class StatisticsCalculator:
    DEFAULT_VALUE = 0

    @staticmethod
    def get_average(numbers):
        if not numbers:
            return StatisticsCalculator.DEFAULT_VALUE
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = StatisticsCalculator()
    data1 = [10, 20, 30, 40, 50]
    average1 = calculator.get_average(data1)
    print(f"The average of {data1} is: {average1}")
    data2 = [5, 15, 25]
    average2 = calculator.get_average(data2)
    print(f"The average of {data2} is: {average2}")
    data3 = []
    average3 = calculator.get_average(data3)
    print(f"The average of {data3} is: {average3}")