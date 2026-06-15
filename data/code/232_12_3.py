class SequenceGenerator:
    def generate_and_print_geometric_sequence(self, start, multiplier, n):
        current_term = start
        for _ in range(n):
            print(current_term)
            current_term *= multiplier
if __name__ == '__main__':
    generator = SequenceGenerator()
    start_value = 2
    multiplier_value = 1.5
    number_of_terms = 5
    generator.generate_and_print_geometric_sequence(start_value, multiplier_value, number_of_terms)