class SequenceGenerator:
    def generate_and_print(self, initial_terms, M):
        sequence = list(initial_terms)
        if len(sequence) < M:
            for i in range(len(sequence), M):
                sequence.append(sequence[-1] if sequence else 0)
        for term in sequence[:M]:
            print(term)
if __name__ == '__main__':
    generator = SequenceGenerator()
    initial_terms = [2, 4, 6]
    M = 10
    generator.generate_and_print(initial_terms, M)