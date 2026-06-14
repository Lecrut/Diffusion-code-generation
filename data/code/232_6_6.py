class SequenceGenerator:
    def generate_and_print(self, initial_terms, m):
        sequence = list(initial_terms)
        if len(sequence) < m:
            remaining_terms = m - len(sequence)
            for i in range(len(sequence), m):
                sequence.append(sequence[-1] if sequence else 0)
        print(*(sequence[:m]))
if __name__ == '__main__':
    generator = SequenceGenerator()
    initial_terms1 = [1, 2, 3]
    m1 = 7
    print("Sequence 1:")
    generator.generate_and_print(initial_terms1, m1)
    initial_terms2 = [5, 10]
    m2 = 5
    print("\nSequence 2:")
    generator.generate_and_print(initial_terms2, m2)
    initial_terms3 = [100]
    m3 = 4
    print("\nSequence 3:")
    generator.generate_and_print(initial_terms3, m3)