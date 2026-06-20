class MathOperations:
    MINUS_ONE = 1

    @staticmethod
    def subtract_fixed_values():
        return 100 - MathOperations.MINUS_ONE

if __name__ == '__main__':
    result = MathOperations.subtract_fixed_values()
    print(result)