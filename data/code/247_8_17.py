class Summation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def compute_sum(self):
        return self.x + self.y

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    calculator = Summation(num1, num2)
    result = calculator.compute_sum()
    print(result)