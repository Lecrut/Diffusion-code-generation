class SequenceSumCalculator:
    @staticmethod
    def calculate_sum(sequence):
        if not sequence:
            return 0
        else:
            return sequence[0] + SequenceSumCalculator.calculate_sum(sequence[1:])

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    result = SequenceSumCalculator.calculate_sum(sample_sequence)
    print(result)