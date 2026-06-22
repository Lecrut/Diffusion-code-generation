class DoublingSequenceGenerator:
    def __init__(self, num_terms):
        self.num_terms = num_terms

    def generate_sequence(self):
        return [2**i for i in range(1, self.num_terms + 1)]

if __name__ == '__main__':
    generator = DoublingSequenceGenerator(5)
    result = generator.generate_sequence()
    print(result)