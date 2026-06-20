from datetime import date

def are_dates_same(date1: date, date2: date) -> bool:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise TypeError('Both arguments must be instances of the date class')
    return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day

if __name__ == '__main__':
    try:
        print(are_dates_same(date(2023, 4, 1), date(2023, 4, 1)))
        print(are_dates_same(date(2023, 4, 1), date(2023, 4, 2)))
    except TypeError as e:
        print(e)