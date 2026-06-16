class NumberOperations:
    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    operations = NumberOperations()
    result1 = operations.subtract(10, 4)
    print(result1)
    result2 = operations.subtract(50, 25)
    print(result2)