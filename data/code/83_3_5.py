from datetime import date

def are_dates_equal(d1: date, d2: date) -> bool:
    return d1 == d2
if __name__ == '__main__':
    print(are_dates_equal(date(2023, 10, 5), date(2023, 10, 5)))
    print(are_dates_equal(date(2023, 10, 5), date(2023, 10, 6)))