class EvenNumberGenerator:
    def generate(self, upper_bound):
        for num in range(2, upper_bound + 1, 2):
            yield num

if __name__ == '__main__':
    gen = EvenNumberGenerator()
    print(list(gen.generate(10)))