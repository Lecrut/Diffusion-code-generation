class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numbers")
        return self._add_helper(a, b)

    def _add_helper(self, a, b):
        return a + b

if __name__ == '__main__':
    calculator = Calculator()
    result = calculator.add(5, 3)
    print(result)