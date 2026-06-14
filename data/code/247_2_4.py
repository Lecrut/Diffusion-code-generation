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
    print(calc.add(5, 3))
    print(calc.add("hello", 3))
    print(calc.add(10.5, 2.5))
    print(calc.add(10, "error"))