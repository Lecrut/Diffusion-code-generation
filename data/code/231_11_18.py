import itertools

class PatternGenerator:
    def __init__(self, sequence_length):
        self.sequence_length = sequence_length
        self.pattern = list(enumerate(itertools.cycle('XY'), start=1))[:sequence_length]

    def get_pattern(self):
        return self.pattern

if __name__ == '__main__':
    generator = PatternGenerator(5)
    result = generator.get_pattern()
    print(result)