class BitwiseOperations:
    @staticmethod
    def bitwise_and(num1, num2):
        if not all(isinstance(i, int) for i in [num1, num2]):
            raise TypeError("Both inputs must be integers")
        return num1 & num2

if __name__ == '__main__':
    result = BitwiseOperations.bitwise_and(10, 5)
    print(result)