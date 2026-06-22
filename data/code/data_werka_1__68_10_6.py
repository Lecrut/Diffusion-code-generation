class NumberComparator:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def validate_numbers(self) -> None:
        if not isinstance(self.num1, int) or not isinstance(self.num2, int):
            raise ValueError("Both numbers must be integers.")

    def calculate_difference(self) -> int:
        self.validate_numbers()
        return abs(self.num1 - self.num2)

if __name__ == '__main__':
    num1 = 15
    num2 = 8
    comparator = NumberComparator(num1, num2)
    print(comparator.calculate_difference())