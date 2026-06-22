class LengthCalculator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def calculate_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    len_calc = LengthCalculator(15, 9)
    print(len_calc.calculate_difference())