class AverageCalculator:
    DEFAULT_VALUE = 0

    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return AverageCalculator.DEFAULT_VALUE
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_data1 = (10, 20, 30, 40, 50)
    average1 = calculator.calculate_average(sample_data1)
    print(f"The average of {sample_data1} is: {average1}")
    sample_data2 = (5, 15, 25)
    average2 = calculator.calculate_average(sample_data2)
    print(f"The average of {sample_data2} is: {average2}")
    sample_data3 = ()
    average3 = calculator.calculate_average(sample_data3)
    print(f"The average of {sample_data3} is: {average3}")