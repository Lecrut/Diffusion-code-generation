from datetime import date

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date3 = date(2023, 7, 4)
    date4 = date(2023, 8, 15)
    print(days_between_dates(date3, date4))