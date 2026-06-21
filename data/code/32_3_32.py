class StringLengthCalculator:
    @staticmethod
    def calculate_total_length(strings):
        return sum(len(s) for s in strings)

if __name__ == '__main__':
    sample_values = ["hello", "world", "example", "code"]
    result = StringLengthCalculator.calculate_total_length(sample_values)
    print(result)