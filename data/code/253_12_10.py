class FindTheMiddleValueAmongThreeCalculator:
    def get_middle(self, a, b, c):
        numbers = sorted([a, b, c])
        return numbers[1]

if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    print(calculator.get_middle(5, 2, 8))