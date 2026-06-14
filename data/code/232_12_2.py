class SequenceGenerator:
    def generate_and_print_geometric_sequence(self, start, multiplier, terms):
        current_term = start
        for _ in range(terms):
            print(current_term)
            current_term *= multiplier
if __name__ == '__main__':
    generator = SequenceGenerator()
    generator.generate_and_print_geometric_sequence(2, 1.5, 5)