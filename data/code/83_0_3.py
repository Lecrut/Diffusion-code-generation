import datetime
def are_dates_identical(date1: datetime.date, date2: datetime.date) -> bool:
    return date1 == date2
if __name__ == '__main__':
    d1 = datetime.date(2023, 10, 26)
    d2 = datetime.date(2023, 10, 26)
    d3 = datetime.date(2023, 10, 27)
    d4 = datetime.date(2023, 10, 26)
    print(f"d1 and d2 are identical: {are_dates_identical(d1, d2)}")
    print(f"d1 and d3 are identical: {are_dates_identical(d1, d3)}")
    print(f"d1 and d4 are identical: {are_dates_identical(d1, d4)}")
    print(f"d2 and d3 are identical: {are_dates_identical(d2, d3)}")
    print(f"d3 and d4 are identical: {are_dates_identical(d3, d4)}")