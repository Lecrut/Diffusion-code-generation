from datetime import date

def days_between_dates(date1, date2):
    delta = date2 - date1
    return abs(delta.days)

if __name__ == '__main__':
    start_date = date(2020, 2, 28)
    end_date = date(2024, 3, 1)
    print(days_between_dates(start_date, end_date))