class SequenceGenerator:
    def generate_and_print(self, initial_terms, m):
        sequence = list(initial_terms)
        if len(sequence) < m:
            remaining_terms = m - len(sequence)
            for i in range(len(sequence), m):
                sequence.append(sequence[-1] if sequence else 0)
        for term in sequence[:m]:
            print(term)
if __name__ == '__main__':
    generator = SequenceGenerator()
    initial_terms_1 = [2, 4, 6]
    m_1 = 7
    print("Sequence 1:")
    generator.generate_and_print(initial_terms_1, m_1)
    initial_terms_2 = [1, 1, 2, 3]
    m_2 = 5
    print("\nSequence 2:")
    generator.generate_and_print(initial_terms_2, m_2)
    initial_terms_3 = [10, 20]
    m_3 = 4
    print("\nSequence 3:")
    generator.generate_and_print(initial_terms_3, m_3)