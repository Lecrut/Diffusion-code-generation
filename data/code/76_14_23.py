from datetime import date

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = date(2023, 5, 1)
    date2 = date(2023, 4, 1)
    print(days_between_dates(date1, date2))