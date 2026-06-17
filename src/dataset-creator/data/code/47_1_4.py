class IntegerMultiplier:
    def __init__(self):
        pass
    def multiply(self, num1, num2) -> int:
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            return int(num1) * int(num2)
        raise TypeError("Both operands must be numeric values.")
if __name__ == '__main__':
    multiplier = IntegerMultiplier()
    result = multiplier.multiply(4, 5)
    print(result)