class MonthDifferenceCalculator:

    def __init__(self):
        self.month_map = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

    def calculate_difference(self, month1_name, month2_name):
        try:
            month1 = self.month_map[month1_name.lower()]
            month2 = self.month_map[month2_name.lower()]
            return abs(month1 - month2)
        except KeyError:
            return 'Invalid month name'
if __name__ == '__main__':
    calculator = MonthDifferenceCalculator()
    result1 = calculator.calculate_difference('january', 'july')
    result2 = calculator.calculate_difference('november', 'march')
    print(result1)
    print(result2)