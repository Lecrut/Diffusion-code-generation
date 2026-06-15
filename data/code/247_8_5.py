class Summation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    summer = Summation(num1, num2)
    result = summer.add()
    print(result)