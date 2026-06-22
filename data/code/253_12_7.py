class FindTheMiddleValueAmongThreeCalculator:
    def find_middle(self, x, y, z):
        numbers = sorted([x, y, z])
        return numbers[1]

if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    a_val = 3
    b_val = 7
    c_val = 5
    result = calculator.find_middle(a_val, b_val, c_val)
    print(result)