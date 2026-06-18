class StatisticsCalculator:
    def find_average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    data1 = [10, 20, 30, 40, 50]
    average1 = calculator.find_average(data1)
    print(f"The average of {data1} is: {average1}")
    data2 = [5, 15, 25]
    average2 = calculator.find_average(data2)
    print(f"The average of {data2} is: {average2}")
    data3 = [100]
    average3 = calculator.find_average(data3)
    print(f"The average of {data3} is: {average3}")
    data4 = []
    average4 = calculator.find_average(data4)
    print(f"The average of {data4} is: {average4}")