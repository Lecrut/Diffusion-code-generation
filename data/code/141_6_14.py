class BitwiseOperations:
    def __init__(self):
        self.sample_values = [0b1010, 0b0101]

    def perform_operations(self, a: int, b: int) -> tuple:
        return a & b, a | b, ~a

if __name__ == '__main__':
    bitwise_ops = BitwiseOperations()
    result_and, result_or, result_not = bitwise_ops.perform_operations(*bitwise_ops.sample_values)
    print(f"AND: {result_and}, OR: {result_or}, NOT: {result_not}")