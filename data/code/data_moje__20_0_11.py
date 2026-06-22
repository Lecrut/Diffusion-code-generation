class ParityChecker:
    MODULUS = 2

    @staticmethod
    def is_even(value: int) -> bool:
        return value % ParityChecker.MODULUS == 0

if __name__ == '__main__':
    print(ParityChecker.is_even(100))
    print(ParityChecker.is_even(101))
    print(ParityChecker.is_even(0))
    print(ParityChecker.is_even(-50))
    print(ParityChecker.is_even(7))