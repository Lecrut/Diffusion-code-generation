class NumericOperations:
    @staticmethod
    def multiply_numbers(a: float, b: float) -> float:
        return a * b

if __name__ == '__main__':
    result = NumericOperations.multiply_numbers(3.5, 2.0)
    print(result)