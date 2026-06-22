class GrowingNumbersGenerator:
    def __init__(self, max_value):
        self.max_value = max_value

    def generate_numbers(self):
        for i in range(1, self.max_value + 1):
            yield i

if __name__ == '__main__':
    generator = GrowingNumbersGenerator(50)
    print(list(generator.generate_numbers()))