import datetime
class DateUtils:
    @staticmethod
    def calculate_difference(date1: datetime.date, date2: datetime.date) -> datetime.timedelta:
        return date2 - date1
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 10)
    difference = DateUtils.calculate_difference(date_a, date_b)
    print(f"Date A: {date_a}")
    print(f"Date B: {date_b}")
    print(f"Difference: {difference}")