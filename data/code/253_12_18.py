class FindTheMiddleValueAmongThreeCalculator:
    def find_middle(self, a, b, c):
        numbers = sorted([a, b, c])
        return numbers[1]

if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    a_val = 5
    b_val = 2
    c_val = 8
    result = calculator.find_middle(a_val, b_val, c_val)
    print(result)