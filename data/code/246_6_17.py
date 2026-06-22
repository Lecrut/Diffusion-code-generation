import sys

class Calculator:
    def __init__(self):
        self.A = 5
        self.B = 10

    def get_total(self):
        return self.A + self.B

if __name__ == '__main__':
    calc = Calculator()
    total = calc.get_total()
    sys.stdout.write(str(total))