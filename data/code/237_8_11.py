class SequenceGenerator:

    def __init__(self):
        self.sequence = [1, 1]

    def next_term(self):
        next_value = sum(self.sequence[-2:]) + 1
        self.sequence.append(next_value)
        return next_value
if __name__ == '__main__':
    generator = SequenceGenerator()
    for _ in range(8):
        print(generator.next_term())