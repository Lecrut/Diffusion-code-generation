class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def add(self):
        try:
            num1 = float(self.value1)
            num2 = float(self.value2)
            return num1 + num2
        except ValueError:
            return "Error: Invalid input. Please enter numeric values."

if __name__ == '__main__':
    calc1 = Calculator(10, 5)
    print(calc1.add())
    
    calc2 = Calculator("hello", 5)
    print(calc2.add())
    
    calc3 = Calculator(3.5, 2.1)
    print(calc3.add())
    
    calc4 = Calculator("a", "b")
    print(calc4.add())