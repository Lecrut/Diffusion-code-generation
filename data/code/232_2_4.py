import itertools

class SequenceGenerator:
    def __init__(self, start=1):
        self.start = start

    def generate_sequence(self, count):
        return list(itertools.islice(itertools.count(self.start), count))

if __name__ == '__main__':
    generator = SequenceGenerator()
    sequence = generator.generate_sequence(20)
    for number in sequence:
        print(number)