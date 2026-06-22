class SequenceGenerator:
    def generate_sequence(self, initial_terms, m):
        sequence = list(initial_terms)
        if len(sequence) < m:
            remaining_terms = m - len(sequence)
            for i in range(len(sequence), m):
                next_term = sequence[-1] + 1
                sequence.append(next_term)
        return sequence[:m]

if __name__ == '__main__':
    generator = SequenceGenerator()
    initial_terms_1 = [100]
    m_1 = 15
    print("Sequence 1:", generator.generate_sequence(initial_terms_1, m_1))