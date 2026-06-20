class MultiplicationHelper:
    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

if __name__ == '__main__':
    result = MultiplicationHelper.multiply(5, 10)
    print(result)
    result2 = MultiplicationHelper.multiply(3.5, 2)
    print(result2)