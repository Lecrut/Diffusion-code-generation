class NumberOperations:
    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    operations = NumberOperations()
    result1 = operations.subtract(10, 4)
    print(f"10 - 4 = {result1}")
    result2 = operations.subtract(5.5, 2.5)
    print(f"5.5 - 2.5 = {result2}")