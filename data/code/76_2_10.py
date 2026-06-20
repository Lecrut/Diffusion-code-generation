from datetime import date

def days_between_dates(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    start_date = date(2023, 1, 1)
    end_date = date(2023, 1, 31)
    print(days_between_dates(start_date, end_date))