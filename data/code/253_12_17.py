class FindTheMiddleValueAmongThreeCalculator:

    def find_middle_value(self, a, b, c):
        if a <= b <= c or c <= b <= a:
            return b
        elif b <= a <= c or c <= a <= b:
            return a
        else:
            return c
if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    result1 = calculator.find_middle_value(5, 2, 8)
    print(result1)
    result2 = calculator.find_middle_value(10, 20, 30)
    print(result2)
    result3 = calculator.find_middle_value(7, 1, 4)
    print(result3)