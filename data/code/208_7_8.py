class MeanCalculator:
    @staticmethod
    def compute_mean(data):
        if not data:
            return None
        total = sum(data)
        count = len(data)
        return total / count

if __name__ == '__main__':
    calculator = MeanCalculator()
    sample_data = [10, 20, 30, 40, 50]
    mean_value = calculator.compute_mean(sample_data)
    print(mean_value)
    sample_data_2 = [1.5, 2.5, 3.5, 4.5]
    mean_value_2 = calculator.compute_mean(sample_data_2)
    print(mean_value_2)
    empty_data = []
    mean_value_empty = calculator.compute_mean(empty_data)
    print(mean_value_empty)