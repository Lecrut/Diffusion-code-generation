class SequenceGenerator:
    def generate_and_print_geometric_sequence(self, start, multiplier):
        current_term = start
        sequence = []
        while current_term < 100:
            sequence.append(current_term)
            current_term *= multiplier
        print("Geometric Sequence:")
        for term in sequence:
            print(term)
if __name__ == '__main__':
    generator = SequenceGenerator()
    generator.generate_and_print_geometric_sequence(2, 1.5)