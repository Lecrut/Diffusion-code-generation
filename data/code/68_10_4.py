class NumberComparator:
    def __init__(self, num1: int, num2: int):
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError("Both numbers must be integers.")
        self.num1 = num1
        self.num2 = num2

    def calculate_difference(self) -> int:
        return abs(self.num1 - self.num2)

if __name__ == '__main__':
    try:
        comparator = NumberComparator(15, 8)
        print(comparator.calculate_difference())
    except ValueError as e:
        print(e)