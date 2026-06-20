import datetime

def are_dates_identical(date1: datetime.datetime, date2: datetime.datetime) -> bool:
    return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day

if __name__ == '__main__':
    sample_date1 = datetime.datetime(2023, 10, 26, 12, 0, 0)
    sample_date2 = datetime.datetime(2023, 10, 26, 14, 0, 0)
    sample_date3 = datetime.datetime(2023, 11, 26, 12, 0, 0)
    
    print(f"Comparing {sample_date1} and {sample_date2}: {are_dates_identical(sample_date1, sample_date2)}")
    print(f"Comparing {sample_date1} and {sample_date3}: {are_dates_identical(sample_date1, sample_date3)}")