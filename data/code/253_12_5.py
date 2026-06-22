class FindTheMiddleValueAmongThreeCalculator:
    def find_middle_value(self, a, b, c):
        return sorted([a, b, c])[1]

if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    print(calculator.find_middle_value(5, 3, 9))