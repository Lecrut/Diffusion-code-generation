import datetime
def are_dates_identical(date1, date2):
    return (date1.year == date2.year and
            date1.month == date2.month and
            date1.day == date2.day)
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 10, 26)
    date_b = datetime.datetime(2023, 10, 26)
    date_c = datetime.datetime(2023, 10, 27)
    date_d = datetime.datetime(2024, 10, 26)
    date_e = datetime.datetime(2023, 10, 26)
    print(f"Are {date_a} and {date_b} identical? {are_dates_identical(date_a, date_b)}")
    print(f"Are {date_a} and {date_c} identical? {are_dates_identical(date_a, date_c)}")
    print(f"Are {date_a} and {date_d} identical? {are_dates_identical(date_a, date_d)}")
    print(f"Are {date_a} and {date_e} identical? {are_dates_identical(date_a, date_e)}")