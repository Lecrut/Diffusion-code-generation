class MonthDifferenceCalculator:
    MONTH_NAMES = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    @staticmethod
    def get_month_index(month_name):
        return MonthDifferenceCalculator.MONTH_NAMES.index(month_name.lower().capitalize()) + 1

    @classmethod
    def calculate_difference(cls, month1_name, month2_name):
        month1 = cls.get_month_index(month1_name)
        month2 = cls.get_month_index(month2_name)
        difference = abs(month1 - month2)
        return difference
if __name__ == '__main__':
    calculator = MonthDifferenceCalculator()
    month_a = 'December'
    month_b = 'March'
    result = calculator.calculate_difference(month_a, month_b)
    print(result)