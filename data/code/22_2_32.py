class OddChecker:
    def is_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = OddChecker()
    sample_numbers = [17, 24, -5, 8]
    for num in sample_numbers:
        print(f"Is {num} odd? {checker.is_odd(num)}")