class Calculator:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2
    
    def sum(self) -> int:
        return self.num1 + self.num2

if __name__ == '__main__':
    calc_instance = Calculator(8, 3)
    total = calc_instance.sum()
    print(total)