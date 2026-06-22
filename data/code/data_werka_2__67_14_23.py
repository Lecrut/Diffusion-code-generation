def add_numbers(a, b):
    return a + b

class Calculator:
    def __init__(self, initial_a=0, initial_b=0):
        self.a = initial_a
        self.b = initial_b
    
    def set_values(self, a, b):
        self.a = a
        self.b = b
    
    def compute_sum(self):
        return add_numbers(self.a, self.b)

if __name__ == '__main__':
    calc = Calculator()
    calc.set_values(5, 3)
    print(calc.compute_sum())
    
    calc.set_values(2.5, 4.7)
    print(calc.compute_sum())
    
    calc.set_values(-1, -1)
    print(calc.compute_sum())
    
    calc.set_values(0, 0)
    print(calc.compute_sum())
    
    calc.set_values(100, 200.5)
    print(calc.compute_sum())