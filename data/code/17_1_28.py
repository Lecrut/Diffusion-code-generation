class NumberChecker:

    def __init__(self, number):
        self.number = number

    def check_parity(self):
        return 'Even' if self.number % 2 == 0 else 'Odd'
if __name__ == '__main__':
    numbers_to_check = [42, 17, 0, -3, 8]
    for num in numbers_to_check:
        checker = NumberChecker(num)
        print(f'The number {num} is {checker.check_parity()}.')