class NumberAnalyzer:
    @staticmethod
    def find_largest_number(sequence):
        if not sequence:
            return None
        return max(sequence)

if __name__ == '__main__':
    sample_sequence = [3.14, 2.71, 1.41, 9.81, 6.28]
    largest_number = NumberAnalyzer.find_largest_number(sample_sequence)
    print(largest_number)