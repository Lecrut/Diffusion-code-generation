class SequenceGenerator:

    def __init__(self):
        self.sequence = [1, 1]

    def generate_next_term(self):
        next_term = sum(self.sequence[-2:]) + 1
        self.sequence.append(next_term)

    def get_sequence(self):
        return self.sequence
if __name__ == '__main__':
    generator = SequenceGenerator()
    for _ in range(8):
        generator.generate_next_term()
    result = generator.get_sequence()
    print(result)