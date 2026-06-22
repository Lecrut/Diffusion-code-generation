class FindTheMiddleValueAmongThreeCalculator:
    def find_middle(self, a, b, c):
        if not all(isinstance(i, (int, float)) for i in [a, b, c]):
            raise ValueError("All inputs must be numbers.")
        return sorted([a, b, c])[1]

if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    print(calculator.find_middle(5, 2, 8))