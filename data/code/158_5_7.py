MAX_UPPER_BOUND = 10

class EvenNumberGenerator:
    def generate(self, upper_bound):
        for number in range(2, min(upper_bound + 1, MAX_UPPER_BOUND) + 1, 2):
            yield number

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    print(list(generator.generate(15)))