from datetime import date

def are_dates_same(date1: date, date2: date) -> bool:
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise TypeError('Both arguments must be instances of the date class')
    return date1.year == date2.year and date1.month == date2.month and (date1.day == date2.day)
if __name__ == '__main__':
    try:
        first_date = date(2023, 5, 1)
        second_date = date(2023, 5, 1)
        third_date = date(2023, 5, 2)
        print(are_dates_same(first_date, second_date))
        print(are_dates_same(first_date, third_date))
    except TypeError as e:
        print(e)