class NumberOperations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def perform_operations(a, b):
        return {
            'add': a + b,
            'subtract': a - b,
            'multiply': a * b,
            'divide': None if b == 0 else a / b,
            'modulus': None if b == 0 else a % b
        }

if __name__ == '__main__':
    sample_values = (10, 5)
    operations = NumberOperations(*sample_values).perform_operations(*sample_values)
    print(operations)