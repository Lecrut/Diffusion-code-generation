class AverageCalculator:
    DEFAULT_AVERAGE = 0

    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return AverageCalculator.DEFAULT_AVERAGE
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_values1 = (1, 2, 3, 4, 5)
    average1 = calculator.calculate_average(sample_values1)
    print(f"The average of {sample_values1} is: {average1}")
    
    sample_values2 = (10, 20, 30, 40, 50)
    average2 = calculator.calculate_average(sample_values2)
    print(f"The average of {sample_values2} is: {average2}")
    
    sample_values3 = ()
    average3 = calculator.calculate_average(sample_values3)
    print(f"The average of {sample_values3} is: {average3}")