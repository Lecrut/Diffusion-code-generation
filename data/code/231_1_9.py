import itertools

class PatternGenerator:
    def __init__(self):
        self.pattern = [1, 2, 3]

    def generate_sequence(self, length):
        return list(itertools.islice(itertools.cycle(self.pattern), length))

if __name__ == '__main__':
    generator = PatternGenerator()
    sample_length = 15
    result = generator.generate_sequence(sample_length)
    print(result)