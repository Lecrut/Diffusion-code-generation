import datetime

def are_dates_identical(date1: datetime.date, date2: datetime.date) -> bool:
    return date1 == date2

if __name__ == '__main__':
    sample_date_1 = datetime.date(2023, 11, 5)
    sample_date_2 = datetime.date(2023, 11, 5)
    sample_date_3 = datetime.date(2023, 11, 6)

    print(f"Are {sample_date_1} and {sample_date_2} identical? {are_dates_identical(sample_date_1, sample_date_2)}")
    print(f"Are {sample_date_1} and {sample_date_3} identical? {are_dates_identical(sample_date_1, sample_date_3)}")