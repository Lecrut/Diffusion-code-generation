class MathOperations:
    CONSTANT_A = 5
    CONSTANT_B = 3

    @staticmethod
    def subtract_values(a=CONSTANT_A, b=CONSTANT_B):
        return a - b

if __name__ == '__main__':
    result = MathOperations.subtract_values()
    print(result)