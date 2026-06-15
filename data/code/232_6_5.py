class SequenceGenerator:
    def generate_and_print(self, initial_terms, M):
        sequence = list(initial_terms)
        if len(sequence) < M:
            remaining = M - len(sequence)
            for i in range(len(sequence), M):
                sequence.append(sequence[-1] if sequence else 0)
        for term in sequence[:M]:
            print(term)
if __name__ == '__main__':
    generator = SequenceGenerator()
    initial_terms_1 = [1, 2, 3]
    M_1 = 7
    print("Sequence 1:")
    generator.generate_and_print(initial_terms_1, M_1)
    initial_terms_2 = [5, 10]
    M_2 = 5
    print("\nSequence 2:")
    generator.generate_and_print(initial_terms_2, M_2)
    initial_terms_3 = [100]
    M_3 = 4
    print("\nSequence 3:")
    generator.generate_and_print(initial_terms_3, M_3)