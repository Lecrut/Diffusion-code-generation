class OddEvenChecker:
    def is_odd(self, number):
        return number & 1 == 1

if __name__ == '__main__':
    checker = OddEvenChecker()
    sample_numbers = [3, 4, 7, 10, 15]
    for num in sample_numbers:
        result = checker.is_odd(num)
        print(f"The number {num} is {'Odd' if result else 'Even'}")