class AbsoluteDifference:
    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value

    def get_difference(self):
        return abs(self.first_value - self.second_value)

if __name__ == '__main__':
    diff_calculator = AbsoluteDifference(100, 75)
    print(diff_calculator.get_difference())
    another_diff_calculator = AbsoluteDifference(25, 40)
    print(another_diff_calculator.get_difference())