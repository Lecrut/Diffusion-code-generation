from datetime import date

def date_difference_days(date1, date2):
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError('Both arguments must be instances of datetime.date')
    delta = abs(date2 - date1)
    return delta.days
if __name__ == '__main__':
    date1 = date(2023, 10, 26)
    date2 = date(2023, 11, 26)
    print(date_difference_days(date1, date2))