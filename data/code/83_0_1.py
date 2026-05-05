import datetime
def are_dates_identical(date1: datetime.date, date2: datetime.date) -> bool:
    return date1 == date2
if __name__ == '__main__':
    date_a = datetime.date(2023, 10, 26)
    date_b = datetime.date(2023, 10, 26)
    date_c = datetime.date(2023, 10, 27)
    date_d = datetime.date(2023, 10, 26)
    print(f"Are {date_a} and {date_b} identical? {are_dates_identical(date_a, date_b)}")
    print(f"Are {date_a} and {date_c} identical? {are_dates_identical(date_a, date_c)}")
    print(f"Are {date_a} and {date_d} identical? {are_dates_identical(date_a, date_d)}")
    print(f"Are {date_b} and {date_c} identical? {are_dates_identical(date_b, date_c)}")