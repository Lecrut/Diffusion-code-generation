class SequenceGenerator:
    MAX_ITERATIONS = 5

    @staticmethod
    def generate_and_print_sequence(start, factor):
        sequence = []
        current_term = start
        for _ in range(SequenceGenerator.MAX_ITERATIONS):
            sequence.append(current_term)
            current_term *= factor
        for term in sequence:
            print(term)

if __name__ == '__main__':
    SequenceGenerator.generate_and_print_sequence(1, 2)