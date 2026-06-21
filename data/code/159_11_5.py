class OddNumberGenerator:
    @staticmethod
    def is_odd(number):
        return number % 2 != 0

    @classmethod
    def generate_odds(cls, values):
        for value in values:
            if cls.is_odd(value):
                yield value

if __name__ == '__main__':
    sample_values = [12, 14, 15, 16, 17, 18, 19]
    odd_gen = OddNumberGenerator.generate_odds(sample_values)
    for odd_value in odd_gen:
        print(odd_value)