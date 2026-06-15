class SequenceGenerator:
    def generate_and_print(self, initial_terms, M):
        sequence = list(initial_terms)
        if len(sequence) < M:
            remaining_terms = M - len(sequence)
            generated_terms = []
            for i in range(len(sequence), M):
                if len(sequence) >= 2:
                    diff = sequence[-1] - sequence[-2]
                    next_term = sequence[-1] + diff
                    generated_terms.append(next_term)
                    sequence.append(next_term)
                else:
                    generated_terms.append(sequence[-1])
                    sequence.append(sequence[-1])
            final_sequence = sequence[:M]
        else:
            final_sequence = sequence[:M]
        print("Generated Sequence:")
        for term in final_sequence:
            print(term)
if __name__ == '__main__':
    generator = SequenceGenerator()
    initial_terms_1 = [2, 4]
    M_1 = 7
    print("--- Test Case 1 ---")
    generator.generate_and_print(initial_terms_1, M_1)
    initial_terms_2 = [10]
    M_2 = 5
    print("\n--- Test Case 2 ---")
    generator.generate_and_print(initial_terms_2, M_2)
    initial_terms_3 = [1, 2, 3, 5, 8]
    M_3 = 6
    print("\n--- Test Case 3 ---")
    generator.generate_and_print(initial_terms_3, M_3)