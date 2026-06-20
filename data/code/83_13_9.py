from datetime import date

def are_dates_same(date1: date, date2: date) -> bool:
    if not isinstance(date1, date):
        raise TypeError('First argument must be an instance of the date class')
    if not isinstance(date2, date):
        raise TypeError('Second argument must be an instance of the date class')
    return date1 == date2

if __name__ == '__main__':
    try:
        print(are_dates_same(date(2023, 4, 1), date(2023, 4, 1)))
        print(are_dates_same(date(2023, 4, 1), date(2023, 4, 2)))
    except TypeError as e:
        print(e)