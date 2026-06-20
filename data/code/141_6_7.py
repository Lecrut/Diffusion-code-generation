class FlagOperations:
    @staticmethod
    def and_operation(a: int, b: int) -> int:
        return a & b

    @staticmethod
    def or_operation(a: int, b: int) -> int:
        return a | b

    @staticmethod
    def not_operation(a: int) -> int:
        return ~a

if __name__ == '__main__':
    result_and = FlagOperations.and_operation(5, 3)
    result_or = FlagOperations.or_operation(5, 3)
    result_not = FlagOperations.not_operation(5)

    print(f"AND: {result_and}, OR: {result_or}, NOT: {result_not}")