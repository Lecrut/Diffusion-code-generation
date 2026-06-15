class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except TypeError:
            return "Error: Unsupported types for addition"
if __name__ == '__main__':
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"3.5 + 2.5 = {calc.add(3.5, 2.5)}")
    print(f"10 + 'a' = {calc.add(10, 'a')}")
    print(f"'hello' + 5 = {calc.add('hello', 5)}")