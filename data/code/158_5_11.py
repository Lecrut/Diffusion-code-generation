class EvenNumberGenerator:
    def generate(self, upper_bound):
        for number in range(2, upper_bound + 1, 2):
            yield number

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    print(list(generator.generate(10)))