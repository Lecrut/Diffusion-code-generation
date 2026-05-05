import datetime
class DateUtils:
    @staticmethod
    def calculate_difference_in_days(date1: datetime.date, date2: datetime.date) -> int:
        return abs((date2 - date1).days)
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 10)
    difference = DateUtils.calculate_difference_in_days(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {difference} days")
    date_c = datetime.date(2024, 5, 20)
    date_d = datetime.date(2024, 1, 1)
    difference_2 = DateUtils.calculate_difference_in_days(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {difference_2} days")