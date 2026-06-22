class NumericalSetAnalyzer:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return 0.0
        total_sum = sum(numbers)
        count = len(numbers)
        return total_sum / count

if __name__ == '__main__':
    data_sets = [
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    ]
    analyzer = NumericalSetAnalyzer()
    average_result = analyzer.calculate_average(data_sets)
    print(average_result)