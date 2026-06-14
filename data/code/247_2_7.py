class Calculator:
    def add(self, a, b):
        try:
            return float(a) + float(b)
        except (TypeError, ValueError):
            return "Error: Invalid input types for addition"
if __name__ == '__main__':
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"3.5 + 2.1 = {calc.add(3.5, 2.1)}")
    print(f"abc + 5 = {calc.add('abc', 5)}")
    print(f"10 + 'hello' = {calc.add(10, 'hello')}")
    print(f"None + 5 = {calc.add(None, 5)}")