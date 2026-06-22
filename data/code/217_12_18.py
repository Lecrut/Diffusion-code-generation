class NumberComparator:
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    MODULUS = "modulus"

    @staticmethod
    def calculate_operations(a, b):
        return {
            NumberComparator.ADD: a + b,
            NumberComparator.SUBTRACT: a - b,
            NumberComparator.MULTIPLY: a * b,
            NumberComparator.DIVIDE: None if b == 0 else a / b,
            NumberComparator.MODULUS: None if b == 0 else a % b
        }

if __name__ == '__main__':
    comparator = NumberComparator()
    result = comparator.calculate_operations(10, 5)
    print(result)