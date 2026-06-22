class NumberAnalyzer:
    @staticmethod
    def find_minimum(numbers):
        return min(numbers)

if __name__ == '__main__':
    sample_numbers = [45, 12, 89, 3, 67, 22]
    minimum_value = NumberAnalyzer.find_minimum(sample_numbers)
    print(minimum_value)