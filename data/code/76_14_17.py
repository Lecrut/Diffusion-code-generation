from datetime import date

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date_a = date(2023, 4, 1)
    date_b = date(2023, 6, 15)
    print(days_between_dates(date_a, date_b))