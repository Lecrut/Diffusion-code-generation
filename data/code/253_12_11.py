class FindTheMiddleValueAmongThreeCalculator:
    def find_middle(self, a, b, c):
        numbers = sorted([a, b, c])
        return numbers[1]

if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    result = calculator.find_middle(5, 2, 8)
    print(result)