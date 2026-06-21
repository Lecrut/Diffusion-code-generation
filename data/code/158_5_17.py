class EvenNumberGenerator:
    def generate(self, upper_bound):
        for number in range(2, upper_bound + 1, 2):
            yield number

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    even_numbers_up_to_10 = list(generator.generate(10))
    print(even_numbers_up_to_10)
    even_numbers_up_to_5 = list(generator.generate(5))
    print(even_numbers_up_to_5)