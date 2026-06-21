class StringLengthCalculator:
    @staticmethod
    def total_length_of_strings(strings):
        return sum(len(s) for s in strings)

if __name__ == '__main__':
    sample_values = ["hello", "world", "this", "is", "a", "test"]
    result = StringLengthCalculator.total_length_of_strings(sample_values)
    print(result)