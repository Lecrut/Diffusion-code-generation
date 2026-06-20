from datetime import date

def date_difference_days(date1, date2):
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError('Both inputs must be instances of datetime.date')
    delta = abs(date2 - date1)
    return delta.days
if __name__ == '__main__':
    try:
        date1 = date(2023, 10, 26)
        date2 = date(2023, 11, 26)
        result = date_difference_days(date1, date2)
        print(result)
    except ValueError as e:
        print(e)