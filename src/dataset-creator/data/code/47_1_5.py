class IntegerMultiplier:
    def __init__(self, first_operand: int, second_operand: int):
        self.first_operand = first_operand
        self.second_operand = second_operand
        if not isinstance(first_operand, int) or isinstance(first_operand, bool):
            raise TypeError(f"First operand must be an integer, got {type(first_operand).__name__}")
        if not isinstance(second_operand, int) or isinstance(second_operand, bool):
            raise TypeError(f"Second operand must be an integer, got {type(second_operand).__name__}")
    def validate_range(self, value: int, min_val: int = -10**9, max_val: int = 10**9) -> None:
        if not (min_val <= value <= max_val):
            raise ValueError(f"Value {value} is out of valid range ({min_val}, {max_val})")
    def validate_inputs(self) -> None:
        self.validate_range(self.first_operand)
        self.validate_range(self.second_operand)
    def multiply(self) -> int:
        self.validate_inputs()
        return self.first_operand * self.second_operand
if __name__ == '__main__':
    multiplier = IntegerMultiplier(3, 4)
    result = multiplier.multiply()
    print(result)