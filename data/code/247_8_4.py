class Summation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
if __name__ == '__main__':
    value1 = 10
    value2 = 5
    sum_calculator = Summation(value1, value2)
    result = sum_calculator.add()
    print(result)