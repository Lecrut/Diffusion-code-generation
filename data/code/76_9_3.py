import datetime
class DateUtils:
    @staticmethod
    def calculate_date_difference(start_date: datetime.date, end_date: datetime.date) -> int:
        return (end_date - start_date).days
if __name__ == '__main__':
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 10)
    difference1 = DateUtils.calculate_date_difference(date1, date2)
    print(f"Difference between {date1} and {date2}: {difference1} days")
    date3 = datetime.date(2024, 5, 15)
    date4 = datetime.date(2024, 5, 15)
    difference2 = DateUtils.calculate_date_difference(date3, date4)
    print(f"Difference between {date3} and {date4}: {difference2} days")
    date5 = datetime.date(2020, 12, 31)
    date6 = datetime.date(2024, 1, 1)
    difference3 = DateUtils.calculate_date_difference(date5, date6)
    print(f"Difference between {date5} and {date6}: {difference3} days")