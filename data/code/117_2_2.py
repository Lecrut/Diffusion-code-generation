class NumberOperations:
    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    operations = NumberOperations()
    result = operations.subtract(10, 4)
    print(result)