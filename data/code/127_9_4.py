class OddNumberChecker:

    @staticmethod
    def is_odd(num):
        return num & 1 == 1
if __name__ == '__main__':
    checker = OddNumberChecker()
    print(checker.is_odd(3))
    print(checker.is_odd(4))