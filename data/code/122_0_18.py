import statistics

class NumberAnalyzer:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return None
        try:
            return statistics.mean(numbers)
        except TypeError:
            raise ValueError("All elements in the list must be numbers")

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_numbers = [10, 20, 30, 40, 50]
    print(analyzer.calculate_average(sample_numbers))