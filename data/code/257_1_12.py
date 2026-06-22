class NumberAnalyzer:
    MIN_VALUE = float('-inf')
    MAX_VALUE = float('inf')

    @staticmethod
    def validate_numbers(numbers):
        if not numbers:
            raise ValueError("The tuple must contain at least one number.")
        return True

    def find_difference(self, numbers):
        self.validate_numbers(numbers)
        min_num = min(numbers)
        max_num = max(numbers)
        return max_num - min_num

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 4.8, 2.9)
    analyzer = NumberAnalyzer()
    print(analyzer.find_difference(sample_values))