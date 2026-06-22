from datetime import date

def is_weekend(day):
    return day.weekday() >= 5
if __name__ == '__main__':
    test_date1 = date(2023, 10, 29)
    print(is_weekend(test_date1))
    test_date2 = date(2023, 10, 30)
    print(is_weekend(test_date2))
    test_date3 = date(2023, 10, 31)
    print(is_weekend(test_date3))