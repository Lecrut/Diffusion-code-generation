from datetime import date

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)
if __name__ == '__main__':
    date_a = date(2020, 2, 28)
    date_b = date(2020, 3, 1)
    print(days_between_dates(date_a, date_b))
    date_c = date(2019, 2, 28)
    date_d = date(2020, 2, 28)
    print(days_between_dates(date_c, date_d))
    date_e = date(2021, 1, 1)
    date_f = date(2021, 12, 31)
    print(days_between_dates(date_e, date_f))