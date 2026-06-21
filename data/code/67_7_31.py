class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both operands must be numbers.")
        result = a + b
        self.history.append((a, b, result))
        return result

    def clear_history(self):
        self.history.clear()

    def get_last_operation(self):
        if self.history:
            return self.history[-1]
        else:
            raise ValueError("No operations have been performed.")

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.add(5, 3)
        print(f"Result of add(5, 3): {result1}")
        result2 = calc.add(10.5, 7.2)
        print(f"Result of add(10.5, 7.2): {result2}")
        last_operation = calc.get_last_operation()
        print(f"Last operation: {last_operation}")
        calc.clear_history()
        print("History cleared.")
    except ValueError as e:
        print(e)