class SequenceSumCalculator:
    @staticmethod
    def calculate_sum(sequence):
        try:
            return sum(sequence)
        except TypeError as e:
            print(f"Error: {e}")
            return None

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    result = SequenceSumCalculator.calculate_sum(sample_sequence)
    if result is not None:
        print(result)