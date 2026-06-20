class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    result_add = calc.add(5, 3)
    result_subtract = calc.subtract(10, 4)
    
    print("Sum:", result_add)
    print("Difference:", result_subtract)