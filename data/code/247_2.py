class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except TypeError:
            return "Error: Invalid types for addition"
        except Exception:
            return "Error: An unexpected error occurred"
if __name__ == '__main__':
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"3.14 + 2 = {calc.add(3.14, 2)}")
    print(f"'a' + 'b' = {calc.add('a', 'b')}")
    print(f"5 + 'text' = {calc.add(5, 'text')}")