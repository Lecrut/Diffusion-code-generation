class SequenceGenerator:
    def generate_and_print(self, initial_terms, M):
        sequence = list(initial_terms)
        if len(sequence) < M:
            remaining = M - len(sequence)
            for i in range(len(sequence), M):
                next_term = sequence[-1] if sequence else 0
                if not sequence:
                    next_term = initial_terms[0] if initial_terms else 0
                else:
                    next_term = sequence[-1]
                sequence.append(next_term)
        for term in sequence[:M]:
            print(term)
if __name__ == '__main__':
    generator = SequenceGenerator()
    initial_terms_1 = [1, 2]
    M_1 = 5
    print("--- Sequence 1 ---")
    generator.generate_and_print(initial_terms_1, M_1)
    initial_terms_2 = [2, 4, 6]
    M_2 = 7
    print("\n--- Sequence 2 ---")
    generator.generate_and_print(initial_terms_2, M_2)
    initial_terms_3 = [10]
    M_3 = 4
    print("\n--- Sequence 3 ---")
    generator.generate_and_print(initial_terms_3, M_3)
    initial_terms_4 = []
    M_4 = 3
    print("\n--- Sequence 4 ---")
    generator.generate_and_print(initial_terms_4, M_4)