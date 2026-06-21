class OddNumberGenerator:
    def __init__(self, values):
        self.values = values

    @staticmethod
    def is_odd(number):
        return number % 2 != 0

    def generate_odds(self):
        for value in self.values:
            if self.is_odd(value):
                yield value

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    generator = OddNumberGenerator(sample_values)
    for odd_value in generator.generate_odds():
        print(odd_value)