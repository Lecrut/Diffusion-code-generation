class EvenNumberGenerator:
    START = 2
    END = 100

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    def generate_evens(self):
        for num in range(EvenNumberGenerator.START, EvenNumberGenerator.END + 1):
            if self.is_even(num):
                yield num

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    for even_number in generator.generate_evens():
        print(even_number)