import itertools

class RepeatingSequenceGenerator:
    def __init__(self):
        self.sequence = [1, 2, 3]

    def generate_sequence(self, length):
        return list(itertools.islice(itertools.cycle(self.sequence), length))

if __name__ == '__main__':
    generator = RepeatingSequenceGenerator()
    sample_length = 15
    result = generator.generate_sequence(sample_length)
    print(result)