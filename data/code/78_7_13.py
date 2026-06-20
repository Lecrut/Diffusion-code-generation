class MonthDifferenceCalculator:
    def __init__(self):
        self.months = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']

    def get_month_index(self, month_name):
        return self.months.index(month_name) + 1

    def calculate_difference(self, month1, month2):
        index1 = self.get_month_index(month1)
        index2 = self.get_month_index(month2)
        difference = abs(index1 - index2)
        return difference

if __name__ == '__main__':
    calculator = MonthDifferenceCalculator()
    result1 = calculator.calculate_difference('March', 'November')
    print(result1)
    result2 = calculator.calculate_difference(5, 8)
    print(result2)