class ArithmeticOperations:
    MINUEND = 1000000000000000000
    SUBTRAHEND = 500000000000000000

    @staticmethod
    def subtract_large_integers(minuend, subtrahend):
        return minuend - subtrahend

if __name__ == '__main__':
    result = ArithmeticOperations.subtract_large_integers(ArithmeticOperations.MINUEND, ArithmeticOperations.SUBTRAHEND)
    print(result)