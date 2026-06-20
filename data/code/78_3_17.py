class MonthDifferenceCalculator:
    MONTH_MAP = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

    @staticmethod
    def get_month_index(month_name):
        try:
            return MonthDifferenceCalculator.MONTH_MAP[month_name.lower()]
        except KeyError:
            raise ValueError('Invalid month name')

    @staticmethod
    def calculate_difference(month1_name, month2_name):
        month1 = MonthDifferenceCalculator.get_month_index(month1_name)
        month2 = MonthDifferenceCalculator.get_month_index(month2_name)
        return abs(month1 - month2)
if __name__ == '__main__':
    calculator = MonthDifferenceCalculator()
    result = calculator.calculate_difference('july', 'february')
    print(result)