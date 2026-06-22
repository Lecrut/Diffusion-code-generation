class NumberGenerator:
    def __init__(self):
        self.sequence = []

    def generate_sequence(self, limit):
        self.sequence = [i for i in range(1, limit + 1)]

    def print_sequence(self):
        for number in self.sequence:
            print(number)

if __name__ == '__main__':
    generator = NumberGenerator()
    generator.generate_sequence(50)
    generator.print_sequence()