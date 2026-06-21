class EvenNumberGenerator:
    def generate(self, upper_bound):
        number = 2
        while number <= upper_bound:
            yield number
            number += 2

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    even_numbers = list(generator.generate(10))
    print(even_numbers)