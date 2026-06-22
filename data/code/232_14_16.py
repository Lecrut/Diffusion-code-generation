class NumberSequence:
    def __init__(self, iterations=5):
        self.iterations = iterations

    @staticmethod
    def square_number(index):
        return index ** 2

    def generate_sequence(self):
        for i in range(1, self.iterations + 1):
            yield self.square_number(i)

if __name__ == '__main__':
    sequence_generator = NumberSequence()
    for number in sequence_generator.generate_sequence():
        print(number)