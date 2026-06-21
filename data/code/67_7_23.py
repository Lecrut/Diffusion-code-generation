class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both operands must be numbers.")
        result = a + b
        self.history.append((a, b, result))
        return result

    def get_history(self):
        return self.history

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.add(5, 3)
        print(f"Result of add(5, 3): {result1}")
        
        result2 = calc.add(10.5, 7.2)
        print(f"Result of add(10.5, 7.2): {result2}")
        
        history = calc.get_history()
        print("History of operations:")
        for op in history:
            print(f"{op[0]} + {op[1]} = {op[2]}")
    except ValueError as e:
        print(e)