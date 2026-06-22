class AverageCalculator:
    NO_ELEMENTS = 0

    @staticmethod
    def calculate_average(set_of_numbers):
        if not set_of_numbers:
            return None
        total_sum = sum(set_of_numbers)
        count = len(set_of_numbers)
        return total_sum / count if count > 0 else AverageCalculator.NO_ELEMENTS
if __name__ == '__main__':
    sample_set = {1, 2, 3}
    avg_result = AverageCalculator.calculate_average(sample_set)
    print(avg_result)