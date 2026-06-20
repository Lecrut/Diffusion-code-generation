class OddEvenChecker:
    @staticmethod
    def is_odd(number):
        return number % 2 != 0

if __name__ == '__main__':
    test_numbers = [5, -10, 0, 3, -7]
    for num in test_numbers:
        print(f"{num} is odd: {OddEvenChecker.is_odd(num)}")