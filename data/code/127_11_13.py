class OddEvenChecker:
    @staticmethod
    def is_odd(number):
        return number % 2 != 0

if __name__ == '__main__':
    checker = OddEvenChecker()
    print(f"3 is odd: {checker.is_odd(3)}")
    print(f"-4 is odd: {checker.is_odd(-4)}")
    print(f"0 is odd: {checker.is_odd(0)}")
    print(f"17 is odd: {checker.is_odd(17)}")