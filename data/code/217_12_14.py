class NumberComparer:
    DIVISION_BY_ZERO_MESSAGE = 'undefined'

    @staticmethod
    def perform_operations(a, b):
        return {
            'add': a + b,
            'subtract': a - b,
            'multiply': a * b,
            'divide': a / b if b != 0 else NumberComparer.DIVISION_BY_ZERO_MESSAGE,
            'modulus': a % b if b != 0 else NumberComparer.DIVISION_BY_ZERO_MESSAGE
        }

if __name__ == '__main__':
    comparer = NumberComparer()
    result = comparer.perform_operations(10, 5)
    print(result)