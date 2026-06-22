class NumberComparator:
    DIVISION_BY_ZERO = 'undefined'

    @staticmethod
    def calculate_operations(a, b):
        return {
            'add': a + b,
            'subtract': a - b,
            'multiply': a * b,
            'divide': NumberComparator.DIVISION_BY_ZERO if b == 0 else a / b,
            'modulus': NumberComparator.DIVISION_BY_ZERO if b == 0 else a % b
        }

if __name__ == '__main__':
    comparator = NumberComparator()
    result = comparator.calculate_operations(10, 5)
    print(result)