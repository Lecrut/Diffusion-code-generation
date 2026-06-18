class StatisticsCalculator:
    def find_average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_numbers1 = [10, 20, 30, 40, 50]
    average1 = calculator.find_average(sample_numbers1)
    print(f"The average of {sample_numbers1} is: {average1}")
    sample_numbers2 = [5, 15, 25]
    average2 = calculator.find_average(sample_numbers2)
    print(f"The average of {sample_numbers2} is: {average2}")
    sample_numbers3 = [100]
    average3 = calculator.find_average(sample_numbers3)
    print(f"The average of {sample_numbers3} is: {average3}")
    sample_numbers4 = []
    average4 = calculator.find_average(sample_numbers4)
    print(f"The average of {sample_numbers4} is: {average4}")