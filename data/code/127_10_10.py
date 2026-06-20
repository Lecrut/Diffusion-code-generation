class OddEvenChecker:
    def __init__(self):
        self.sample_numbers = [10, 7, 0, -4, 15]

    def is_odd(self, number):
        return number & 1 == 1

    def check_numbers(self):
        for num in self.sample_numbers:
            result = "Odd" if self.is_odd(num) else "Even"
            print(f"Number: {num}, Result: {result}")

if __name__ == '__main__':
    checker = OddEvenChecker()
    checker.check_numbers()