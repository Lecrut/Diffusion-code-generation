import datetime
def are_dates_identical(date1: datetime.datetime, date2: datetime.datetime) -> bool:
    return date1.date() == date2.date()
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 10, 26, 10, 30, 0)
    date_b = datetime.datetime(2023, 10, 26, 15, 45, 0)
    date_c = datetime.datetime(2023, 10, 27, 9, 0, 0)
    date_d = datetime.datetime(2024, 10, 26, 10, 30, 0)
    print(f"Are {date_a} and {date_b} identical? {are_dates_identical(date_a, date_b)}")
    print(f"Are {date_a} and {date_c} identical? {are_dates_identical(date_a, date_c)}")
    print(f"Are {date_a} and {date_d} identical? {are_dates_identical(date_a, date_d)}")
    print(f"Are {date_a} and {date_a} identical? {are_dates_identical(date_a, date_a)}")