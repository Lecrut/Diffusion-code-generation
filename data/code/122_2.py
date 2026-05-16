class NumberAnalyzer:
    def get_average(self, numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_numbers = [10.5, 20.0, 35.5, 15.0]
    average = analyzer.get_average(sample_numbers)
    print(average)