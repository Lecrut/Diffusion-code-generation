class OddChecker:

    @staticmethod
    def is_odd(number):
        return number & 1 == 1
if __name__ == '__main__':
    print(OddChecker.is_odd(7))
    print(OddChecker.is_odd(8))