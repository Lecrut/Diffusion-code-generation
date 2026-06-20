class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2

if __name__ == '__main__':
    calc = Calculator()
    operations = {
        '+': calc.add,
        '-': calc.subtract,
        '*': calc.multiply,
        '/': calc.divide
    }
    
    print(operations['+'](10, 5))
    print(operations['-'](20, 8))
    print(operations['*'](6, 7))