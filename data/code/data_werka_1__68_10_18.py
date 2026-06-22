class NumberComparator:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def _validate_numbers(self) -> bool:
        if not isinstance(self.num1, int) or not isinstance(self.num2, int):
            raise ValueError("Both numbers must be integers.")
        return True

    def calculate_difference(self) -> int:
        if self._validate_numbers():
            return abs(self.num1 - self.num2)

if __name__ == '__main__':
    comparator = NumberComparator(15, 8)
    print(comparator.calculate_difference())