class FindTheMiddleValueAmongThreeCalculator:
    def find_middle(self, a, b, c):
        numbers = sorted([a, b, c])
        return numbers[1]

if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    print(calculator.find_middle(5, 2, 8))
    print(calculator.find_middle(1, 5, 2))
    print(calculator.find_middle(10, 20, 30))
    print(calculator.find_middle(7, 1, 4))