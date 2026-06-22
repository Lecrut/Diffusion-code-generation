class NumberAnalyzer:
    @staticmethod
    def calculate_difference(numbers):
        return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = (3.5, 1.2, 7.8, 0.9)
    difference = NumberAnalyzer.calculate_difference(sample_numbers)
    print(difference)