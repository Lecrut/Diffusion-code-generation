class FindTheMiddleValueAmongThreeCalculator:
    MIN_VALUE = -1000
    MAX_VALUE = 1000

    @staticmethod
    def find_middle_value(a, b, c):
        return sorted([a, b, c])[1]

if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    print(calculator.find_middle_value(5, 3, 8))