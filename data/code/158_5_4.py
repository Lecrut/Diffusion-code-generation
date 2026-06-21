class EvenNumberGenerator:
    def generate(self, upper_bound):
        for num in range(2, upper_bound + 1, 2):
            yield num

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    even_numbers = list(generator.generate(10))
    print(even_numbers)