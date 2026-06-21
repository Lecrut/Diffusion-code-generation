import statistics

class MeanCalculator:
    def calculate_mean(self, numbers):
        if not numbers:
            return None
        return statistics.mean(numbers)

if __name__ == '__main__':
    calculator = MeanCalculator()
    sample_values1 = [1, 2, 3, 4, 5]
    sample_values2 = [10.5, 20.5, 30.5]
    empty_list = []
    
    mean1 = calculator.calculate_mean(sample_values1)
    mean2 = calculator.calculate_mean(sample_values2)
    mean_empty = calculator.calculate_mean(empty_list)
    
    print(f"Mean of {sample_values1}: {mean1}")
    print(f"Mean of {sample_values2}: {mean2}")
    print(f"Mean of {empty_list}: {mean_empty}")