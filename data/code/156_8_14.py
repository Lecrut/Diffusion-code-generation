class AverageCalculator:
    @staticmethod
    def compute_mean(data):
        if not data:
            return 0
        total = sum(data)
        count = len(data)
        return total / count

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_list = [10, 20, 30, 40, 50]
    average = calculator.compute_mean(sample_list)
    print(average)