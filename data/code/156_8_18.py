class AverageCalculator:
    @staticmethod
    def compute_mean(data):
        if not data:
            return 0
        total = sum(data)
        count = len(data)
        return total / count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    calculator = AverageCalculator()
    average = calculator.compute_mean(sample_list)
    print(average)