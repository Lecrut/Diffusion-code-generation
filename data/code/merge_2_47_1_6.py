class Multiplier:
    def __init__(self):
        self.result = 0
    def validate_input(self, a: int, b: int) -> None:
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both operands must be integers.")
        MAX_LIMIT = 10**9
        if a > MAX_LIMIT or b > MAX_LIMIT:
            raise ValueError(f"Input values cannot exceed {MAX_LIMIT}.")
    def multiply(self, a: int, b: int) -> None:
        self.validate_input(a, b)
        self.result = a * b
        print(f"Result of {a} multiplied by {b} is {self.result}.")
if __name__ == '__main__':
    multiplier_instance = Multiplier()
    num1: int = 42
    num2: int = -8
    try:
        multiplier_instance.multiply(num1, num2)
    except (TypeError, ValueError) as e:
        print(f"Error occurred during multiplication: {e}")