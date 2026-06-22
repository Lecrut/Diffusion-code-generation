class NumberSequenceGenerator:
    def __init__(self, start=1, end=50):
        self.start = start
        self.end = end

    def generate_sequence(self):
        return [i for i in range(self.start, self.end + 1)]

if __name__ == '__main__':
    generator = NumberSequenceGenerator()
    sequence = generator.generate_sequence()
    for number in sequence:
        print(number)