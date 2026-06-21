import statistics

class MeanCalculator:
    EMPTY_LIST_MEAN = 0
    
    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            return MeanCalculator.EMPTY_LIST_MEAN
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    calculator = MeanCalculator()
    sample_list = [10, 20, 30, 40, 50]
    empty_list = []
    print(f"Mean of {sample_list}: {calculator.calculate_mean(sample_list)}")
    print(f"Mean of {empty_list}: {calculator.calculate_mean(empty_list)}")