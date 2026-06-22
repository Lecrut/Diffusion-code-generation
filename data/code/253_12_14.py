class FindTheMiddleValueAmongThreeCalculator:
    MIN_VALUE = -1000
    MAX_VALUE = 1000

    @staticmethod
    def find_middle_value(a, b, c):
        if a < b < c or c < b < a:
            return b
        elif b < a < c or c < a < b:
            return a
        else:
            return c

if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    print(calculator.find_middle_value(5, 10, 7))