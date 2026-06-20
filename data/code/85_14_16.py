from datetime import timedelta

class DateDifferenceCalculator:
    WEEKS_PER_DAY = 7
    
    @staticmethod
    def weeks_difference(date1, date2):
        delta = abs((date2 - date1).days)
        return delta // DateDifferenceCalculator.WEEKS_PER_DAY

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    date1 = calculator.date_from_string("2023-01-01")
    date2 = calculator.date_from_string("2023-01-15")
    
    def date_from_string(date_str):
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    
    print(calculator.weeks_difference(date1, date2))