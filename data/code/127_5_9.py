class OddNumberGenerator:
    @staticmethod
    def is_odd(number):
        return number % 2 != 0

    @staticmethod
    def generate_odds(numbers):
        return (num for num in numbers if OddNumberGenerator.is_odd(num))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_generator = OddNumberGenerator.generate_odds(sample_numbers)
    result = list(odd_generator)
    print(result)