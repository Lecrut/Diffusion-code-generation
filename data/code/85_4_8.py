from datetime import date
WEEK_DAYS = 7

def week_difference(date1: date, date2: date) -> int:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError('Both inputs must be instances of date.')
    if date1 > date2:
        date1, date2 = (date2, date1)
    return (date2 - date1).days // WEEK_DAYS

class DateDifferenceCalculator:

    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date

    def calculate_weeks(self) -> int:
        if not isinstance(self.start_date, date) or not isinstance(self.end_date, date):
            raise ValueError('Both start_date and end_date must be instances of date.')
        if self.start_date > self.end_date:
            self.start_date, self.end_date = (self.end_date, self.start_date)
        return (self.end_date - self.start_date).days // WEEK_DAYS
if __name__ == '__main__':
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)
    print('Week difference (function):', week_difference(start_date, end_date))
    calculator = DateDifferenceCalculator(start_date, end_date)
    print('Week difference (class):', calculator.calculate_weeks())