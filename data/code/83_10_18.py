from datetime import datetime

def are_dates_identical(date1: datetime, date2: datetime) -> bool:
    return date1.year == date2.year and date1.month == date2.month and (date1.day == date2.day)
if __name__ == '__main__':
    sample_date1 = datetime(2023, 4, 15)
    sample_date2 = datetime(2023, 4, 15)
    sample_date3 = datetime(2023, 4, 16)
    print(are_dates_identical(sample_date1, sample_date2))
    print(are_dates_identical(sample_date1, sample_date3))