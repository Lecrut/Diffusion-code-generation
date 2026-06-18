class Multiplier:
    def __init__(self, first_value: int, second_value: int):
        self.first_value = first_value
        self.second_value = second_value
        if not isinstance(first_value, int) or not isinstance(second_value, int):
            raise TypeError("Both values must be integers.")
        if abs(self.first_value) > 10**9 or abs(self.second_value) > 10**9:
            raise ValueError("Values must be within the range [-10^9, 10^9].")
    def calculate(self) -> int:
        try:
            return self.first_value * self.second_value
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred during multiplication: {e}")
if __name__ == '__main__':
    multiplier = Multiplier(5, 6)
    result = multiplier.calculate()
    print(result)