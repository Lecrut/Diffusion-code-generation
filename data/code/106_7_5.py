from datetime import date

def years_between_dates(date1: date, date2: date) -> int:
    return abs((date2.year - date1.year) - ((date2.month, date2.day) < (date1.month, date1.day)))

if __name__ == '__main__':
    start_date = date(2010, 5, 15)
    end_date = date(2023, 8, 20)
    print(years_between_dates(start_date, end_date))