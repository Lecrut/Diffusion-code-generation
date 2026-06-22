class NumberComparator:
    def __init__(self, first_number: int, second_number: int):
        self.first_number = first_number
        self.second_number = second_number

    def calculate_difference(self) -> int:
        difference = abs(self.first_number - self.second_number)
        return difference

if __name__ == '__main__':
    num1 = 20
    num2 = 8
    comparator = NumberComparator(num1, num2)
    result = comparator.calculate_difference()
    print(result)