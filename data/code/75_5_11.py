import datetime

class DateDifferenceCalculator:
    @staticmethod
    def calculate_difference(date1: datetime.date, date2: datetime.date) -> int:
        return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 15)
    print(DateDifferenceCalculator.calculate_difference(date1, date2))