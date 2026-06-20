class FlagOperations:
    @staticmethod
    def bitwise_and(a: int, b: int) -> int:
        return a & b

    @staticmethod
    def bitwise_or(a: int, b: int) -> int:
        return a | b

    @staticmethod
    def bitwise_not(a: int) -> int:
        return ~a

if __name__ == '__main__':
    result_and = FlagOperations.bitwise_and(5, 3)
    result_or = FlagOperations.bitwise_or(5, 3)
    result_not = FlagOperations.bitwise_not(5)
    print(f"AND: {result_and}, OR: {result_or}, NOT: {result_not}")