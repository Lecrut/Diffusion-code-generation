class SequenceGenerator:
    def generate_and_print(self, initial_terms, m):
        sequence = list(initial_terms)
        if len(sequence) < m:
            remaining = m - len(sequence)
            for i in range(len(sequence), m):
                sequence.append(sequence[-1] if sequence else 0)
        for term in sequence[:m]:
            print(term)
if __name__ == '__main__':
    generator = SequenceGenerator()
    initial_terms = [2, 4, 6]
    m = 10
    generator.generate_and_print(initial_terms, m)