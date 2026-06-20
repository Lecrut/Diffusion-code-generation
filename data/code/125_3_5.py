class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    print(f"Sum: {calc.add(15, 7)}")
    print(f"Difference: {calc.subtract(15, 7)}")