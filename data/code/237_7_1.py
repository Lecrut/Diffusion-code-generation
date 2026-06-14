class SequenceGenerator:
    def generate_doubling_sequence(self, initial_value, length):
        sequence = []
        current_term = initial_value
        for _ in range(length):
            sequence.append(current_term)
            current_term *= 2
        return sequence
if __name__ == '__main__':
    generator = SequenceGenerator()
    initial = 3
    length = 5
    result = generator.generate_doubling_sequence(initial, length)
    print(result)