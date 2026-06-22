class GeometricSequenceGenerator:
    DEFAULT_START = 5
    DEFAULT_RATIO = 3
    DEFAULT_TERMS = 8

    @staticmethod
    def generate_sequence(start=DEFAULT_START, ratio=DEFAULT_RATIO, terms=DEFAULT_TERMS):
        sequence = []
        current_term = float(start)
        for _ in range(terms):
            sequence.append(current_term)
            current_term *= ratio
        return sequence

if __name__ == '__main__':
    generator = GeometricSequenceGenerator()
    result = generator.generate_sequence()
    print(result)