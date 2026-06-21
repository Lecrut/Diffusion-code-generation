import statistics

class MeanCalculator:
    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = MeanCalculator()
    sample_list = [10, 20, 30, 40, 50]
    empty_list = []
    single_element_list = [99]

    mean1 = calculator.calculate_mean(sample_list)
    mean2 = calculator.calculate_mean(empty_list)
    mean3 = calculator.calculate_mean(single_element_list)

    print(f"Mean of {sample_list}: {mean1}")
    print(f"Mean of {empty_list}: {mean2}")
    print(f"Mean of {single_element_list}: {mean3}")