from datetime import date

def validate_dates(date1: date, date2: date) -> None:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError("Both inputs must be instances of date.")
    if date1 > date2:
        raise ValueError("First date must not be later than the second date.")

def week_difference(date1: date, date2: date) -> int:
    validate_dates(date1, date2)
    return (date2 - date1).days // 7

class DateDifferenceCalculator:
    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date
    
    def calculate_weeks(self) -> int:
        validate_dates(self.start_date, self.end_date)
        return (self.end_date - self.start_date).days // 7

if __name__ == '__main__':
    print(week_difference(date(2023, 1, 1), date(2023, 1, 8)))
    print(week_difference(date(2023, 1, 8), date(2023, 1, 1)))
    print(week_difference(date(2023, 1, 1), date(2023, 2, 1)))
    print(week_difference(date(2023, 12, 25), date(2024, 1, 1)))

    calculator = DateDifferenceCalculator(date(2023, 1, 1), date(2023, 2, 1))
    print(calculator.calculate_weeks())