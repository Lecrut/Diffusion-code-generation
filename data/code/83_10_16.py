import datetime

def are_dates_identical(date1, date2):
    return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day

if __name__ == '__main__':
    date_a = datetime.datetime(2023, 10, 26)
    date_b = datetime.datetime(2023, 10, 26)
    date_c = datetime.datetime(2023, 10, 27)
    
    print(f"Comparing {date_a} and {date_b}: {are_dates_identical(date_a, date_b)}")
    print(f"Comparing {date_a} and {date_c}: {are_dates_identical(date_a, date_c)}")