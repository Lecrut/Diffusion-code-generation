class EvenNumberGenerator:
    def generate(self, upper_bound):
        for num in range(0, upper_bound + 1, 2):
            yield num

if __name__ == '__main__':
    gen = EvenNumberGenerator()
    for even_num in gen.generate(10):
        print(even_num)