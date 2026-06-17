class SequenceAnalyzer:
    @staticmethod
    def count_even_integers(sequence):
        count = 0
        for number in sequence:
            if number % 2 == 0:
                count += 1
        return count
if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = SequenceAnalyzer.count_even_integers(sample_sequence)
    print(result)