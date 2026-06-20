class DivisionOperations:
    DIVIDEND = 100
    DIVISOR = 7

    @staticmethod
    def calculate_quotient():
        return DivisionOperations.DIVIDEND // DivisionOperations.DIVISOR

    @staticmethod
    def calculate_remainder():
        return DivisionOperations.DIVIDEND % DivisionOperations.DIVISOR

if __name__ == '__main__':
    quotient = DivisionOperations.calculate_quotient()
    remainder = DivisionOperations.calculate_remainder()
    print(quotient)
    print(remainder)