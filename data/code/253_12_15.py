class FindTheMiddleValueAmongThreeCalculator:
    def find_middle_value(self, x, y, z):
        numbers = [x, y, z]
        if len(numbers) != 3:
            raise ValueError("Exactly three values are required")
        return sorted(numbers)[1]

if __name__ == '__main__':
    calculator = FindTheMiddleValueAmongThreeCalculator()
    print(calculator.find_middle_value(5, 2, 8))
    print(calculator.find_middle_value(1, 5, 2))
    print(calculator.find_middle_value(10, 20, 30))
    print(calculator.find_middle_value(7, 1, 4))