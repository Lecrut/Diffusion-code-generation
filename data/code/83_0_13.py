import datetime

def are_dates_identical(date1, date2):
    return date1 == date2
if __name__ == '__main__':
    print(are_dates_identical(datetime.date(2023, 4, 1), datetime.date(2023, 4, 1)))
    print(are_dates_identical(datetime.date(2023, 4, 1), datetime.date(2023, 4, 2)))