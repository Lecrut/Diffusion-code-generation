class EvenNumberGenerator:
    def generate(self, upper_bound):
        if not isinstance(upper_bound, int) or upper_bound < 0:
            raise ValueError("Upper bound must be a non-negative integer")
        for number in range(2, upper_bound + 1, 2):
            yield number

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    even_numbers = list(generator.generate(10))
    print(even_numbers)