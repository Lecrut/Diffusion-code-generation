class BitwiseOperation:
    @staticmethod
    def and_operation(num1: int, num2: int) -> int:
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError("Both inputs must be integers")
        return num1 & num2

if __name__ == '__main__':
    result = BitwiseOperation.and_operation(10, 5)
    print(result)