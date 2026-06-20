from datetime import date

def dates_in_same_week(date1: date, date2: date) -> bool:
    return date1.isocalendar()[1] == date2.isocalendar()[1]
if __name__ == '__main__':
    print(dates_in_same_week(date(2023, 4, 1), date(2023, 4, 8)))
    print(dates_in_same_week(date(2023, 4, 1), date(2023, 4, 9)))