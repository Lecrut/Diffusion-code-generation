class NumberAnalyzer:
    def get_average(self, numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_numbers = [10.5, 20.0, 33.5, 40.0, 5.5]
    average = analyzer.get_average(sample_numbers)
    print(average)