class StringLengthCalculator:
    @staticmethod
    def calculate_total_length(strings):
        return sum(len(s) for s in strings)

if __name__ == '__main__':
    sample_values = ["Qwen", "is", "an", "AI", "model"]
    result = StringLengthCalculator.calculate_total_length(sample_values)
    print(result)