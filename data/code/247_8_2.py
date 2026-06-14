class Summation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
if __name__ == '__main__':
    val1 = 10
    val2 = 5
    sum_calculator = Summation(val1, val2)
    result = sum_calculator.add()
    print(result)