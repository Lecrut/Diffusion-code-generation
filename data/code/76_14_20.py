from datetime import date

def days_between_dates(date1, date2):
    delta = abs(date2 - date1)
    return delta.days

if __name__ == '__main__':
    start_date = date(2023, 4, 1)
    end_date = date(2023, 6, 15)
    print(days_between_dates(start_date, end_date))