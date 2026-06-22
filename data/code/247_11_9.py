class MathOperations:
    def add_numbers(self, a, b):
        return a + b

if __name__ == '__main__':
    math = MathOperations()
    result1 = math.add_numbers(5, 3)
    result2 = math.add_numbers(7, 2)
    print(result1)
    print(result2)