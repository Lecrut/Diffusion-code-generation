class GrowingNumbersGenerator:
    def __init__(self, N):
        self.N = N

    def generate_numbers(self):
        for i in range(1, self.N + 1):
            yield i

if __name__ == '__main__':
    generator = GrowingNumbersGenerator(50)
    for number in generator.generate_numbers():
        print(number)