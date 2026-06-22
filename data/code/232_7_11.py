class NumberSequence:
    def __init__(self):
        self.sequence = []

    def generate_sequence(self, limit):
        for i in range(limit):
            self.sequence.append(i**2)

    def print_sequence(self):
        for num in self.sequence:
            print(num)

if __name__ == '__main__':
    seq_gen = NumberSequence()
    seq_gen.generate_sequence(10)
    seq_gen.print_sequence()