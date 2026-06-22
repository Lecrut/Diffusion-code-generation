class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def sum_values(self):
        return self.value1 + self.value2

if __name__ == '__main__':
    calc = Calculator(7, 3)
    total_sum = calc.sum_values()
    print(total_sum)