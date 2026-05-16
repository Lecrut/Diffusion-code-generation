import datetime
class DateUtils:
    @staticmethod
    def calculate_difference(date1: datetime.date, date2: datetime.date) -> int:
        return abs((date2 - date1).days)
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2024, 1, 1)
    difference = DateUtils.calculate_difference(date_a, date_b)
    print(difference)