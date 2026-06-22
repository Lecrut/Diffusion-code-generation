class ArithmeticProgressionGenerator:
    def __init__(self, start=5, difference=3):
        self.start = start
        self.difference = difference

    def generate_sequence(self, terms=15):
        return [self.start + i * self.difference for i in range(terms)]

if __name__ == '__main__':
    generator = ArithmeticProgressionGenerator()
    progression = generator.generate_sequence()
    print(progression)