class NumberComparator:
    def __init__(self, num1: int, num2: int):
        self.first_number = num1
        self.second_number = num2

    def calculate_difference(self) -> int:
        return abs(self.first_number - self.second_number)

if __name__ == '__main__':
    sample_num1 = 15
    sample_num2 = 9
    comparator = NumberComparator(sample_num1, sample_num2)
    difference = comparator.calculate_difference()
    print(difference)