class SequenceCalculator:
    @staticmethod
    def calculate_sequence_sum(numbers):
        return sum([num for num in numbers])

if __name__ == '__main__':
    sample_data = [1, 5, 10, 15, 20]
    result = SequenceCalculator.calculate_sequence_sum(sample_data)
    print(result)