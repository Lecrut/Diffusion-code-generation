class FindTheMiddleValueAmongThreeCalculator:
    MIDDLE_INDEX = 1

    @staticmethod
    def find_middle(a, b, c):
        numbers = sorted([a, b, c])
        return numbers[FindTheMiddleValueAmongThreeCalculator.MIDDLE_INDEX]
if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    print(calculator.find_middle(1, 5, 2))
    print(calculator.find_middle(10, 20, 30))
    print(calculator.find_middle(7, 7, 7))
    print(calculator.find_middle(1, 100, 50))