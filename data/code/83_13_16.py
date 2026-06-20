from datetime import date

def are_dates_same(date1: date, date2: date) -> bool:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise TypeError('Both arguments must be instances of date')
    return date1 == date2
if __name__ == '__main__':
    print(are_dates_same(date(2023, 10, 5), date(2023, 10, 5)))
    print(are_dates_same(date(2023, 10, 5), date(2023, 10, 6)))