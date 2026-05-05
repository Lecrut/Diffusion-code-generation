import datetime
def are_dates_identical(date1, date2):
    return date1.date() == date2.date()
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 10, 26, 14, 30, 0)
    date_b = datetime.datetime(2023, 10, 26, 9, 0, 0)
    date_c = datetime.datetime(2023, 10, 27, 10, 0, 0)
    date_d = datetime.datetime(2024, 1, 1, 0, 0, 0)
    print(f"Are {date_a} and {date_b} identical? {are_dates_identical(date_a, date_b)}")
    print(f"Are {date_a} and {date_c} identical? {are_dates_identical(date_a, date_c)}")
    print(f"Are {date_a} and {date_d} identical? {are_dates_identical(date_a, date_d)}")
    print(f"Are {date_b} and {date_c} identical? {are_dates_identical(date_b, date_c)}")