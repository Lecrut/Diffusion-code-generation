class NumberOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

if __name__ == '__main__':
    num1 = 7
    num2 = 8
    result = NumberOperations.add_numbers(num1, num2)
    print(result)