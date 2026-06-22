class ArithmeticProgression:
    def __init__(self, start=5, difference=3):
        self.start = start
        self.difference = difference

    def generate_sequence(self, terms=15):
        return [self.start + i * self.difference for i in range(terms)]

if __name__ == '__main__':
    generator = ArithmeticProgression(start=5, difference=3)
    progression = generator.generate_sequence(15)
    print(progression)