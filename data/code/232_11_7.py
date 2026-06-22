class GrowingSequenceGenerator:
    START = 1
    FACTOR = 2

    @staticmethod
    def generate_sequence(iterations):
        current_term = GrowingSequenceGenerator.START
        for _ in range(iterations):
            yield current_term
            current_term *= GrowingSequenceGenerator.FACTOR

if __name__ == '__main__':
    generator = GrowingSequenceGenerator()
    sequence = list(generator.generate_sequence(5))
    for term in sequence:
        print(term)