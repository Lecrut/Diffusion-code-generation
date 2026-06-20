import datetime

def are_dates_identical(date1: datetime.date, date2: datetime.date) -> bool:
    return date1 == date2

if __name__ == '__main__':
    sample_date1 = datetime.date(2023, 10, 26)
    sample_date2 = datetime.date(2023, 10, 27)
    print(f"Are {sample_date1} and {sample_date2} identical? {are_dates_identical(sample_date1, sample_date2)}")