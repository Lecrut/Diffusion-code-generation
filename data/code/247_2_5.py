class Calculator:
    def add(self, a, b):
        try:
            result = float(a) + float(b)
            return result
        except (ValueError, TypeError):
            return "Error: Invalid input types for addition"
if __name__ == '__main__':
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"'a' + 5 = {calc.add('a', 5)}")
    print(f"3.5 + 2.5 = {calc.add(3.5, 2.5)}")
    print(f"10 + 'text' = {calc.add(10, 'text')}")
    print(f"None + 5 = {calc.add(None, 5)}")