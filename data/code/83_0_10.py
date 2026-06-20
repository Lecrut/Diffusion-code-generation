import datetime

def are_dates_identical(date1: datetime.date, date2: datetime.date) -> bool:
    return date1 == date2

if __name__ == '__main__':
    DATE_A = datetime.date(2023, 10, 26)
    DATE_B = datetime.date(2023, 10, 26)
    DATE_C = datetime.date(2023, 10, 27)
    DATE_D = datetime.date(2023, 10, 26)

    print(f"Are {DATE_A} and {DATE_B} identical? {are_dates_identical(DATE_A, DATE_B)}")
    print(f"Are {DATE_A} and {DATE_C} identical? {are_dates_identical(DATE_A, DATE_C)}")
    print(f"Are {DATE_A} and {DATE_D} identical? {are_dates_identical(DATE_A, DATE_D)}")