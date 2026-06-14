class SequenceGenerator:
    def generate_arithmetic_progression(self, a1, d, n):
        sequence = []
        for i in range(n):
            term = a1 + i * d
            sequence.append(term)
        return sequence
if __name__ == '__main__':
    generator = SequenceGenerator()
    start_value = 2
    common_difference = 3
    number_of_elements = 5
    result = generator.generate_arithmetic_progression(start_value, common_difference, number_of_elements)
    print(result)