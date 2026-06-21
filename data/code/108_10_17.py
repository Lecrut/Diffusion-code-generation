import datetime

def validate_date(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Year, month, and day must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31")
    return True

def get_day_of_week(year, month, day):
    validate_date(year, month, day)
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_day_name(self):
        validate_date(self.year, self.month, self.day)
        date_obj = datetime.date(self.year, self.month, self.day)
        return date_obj.strftime("%A")

if __name__ == '__main__':
    result = get_day_of_week(2024, 1, 1)
    print(result)

    analyzer = DateAnalyzer(2024, 1, 1)
    print(analyzer.get_day_name())