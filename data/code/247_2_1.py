class Calculator:
    def add(self, a, b):
        try:
            return float(a) + float(b)
        except (ValueError, TypeError):
            return "Error: Invalid input types"
if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.add("10", 2))
    print(calc.add(4.5, 2.5))
    print(calc.add("hello", 1))
    print(calc.add(10, "text"))