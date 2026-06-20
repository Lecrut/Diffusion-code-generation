from datetime import date

def are_dates_same(date1: date, date2: date) -> bool:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise TypeError('Both arguments must be instances of the date class')
    return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day

if __name__ == '__main__':
    try:
        date_a = date(2023, 7, 4)
        date_b = date(2023, 7, 5)
        print(are_dates_same(date_a, date_b))
        print(are_dates_same(date_a, date_a))
    except TypeError as e:
        print(e)