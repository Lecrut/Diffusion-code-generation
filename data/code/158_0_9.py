class EvenNumberGenerator:
    def __init__(self, max_value):
        self.max_value = max_value

    def generate_even_numbers(self):
        return [x for x in range(1, self.max_value + 1) if x % 2 == 0]

if __name__ == '__main__':
    generator = EvenNumberGenerator(50)
    even_numbers = generator.generate_even_numbers()
    print(even_numbers)