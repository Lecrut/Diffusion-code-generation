class NumberOperations:
    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    operations = NumberOperations()
    num1 = 25
    num2 = 10
    result = operations.subtract(num1, num2)
    print(result)