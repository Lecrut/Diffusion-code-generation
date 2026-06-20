from datetime import date, timedelta

def next_month_date(year, month):
    if month == 12:
        return date(year + 1, 1, 1)
    else:
        _, last_day = calendar.monthrange(year, month)
        try:
            return date(year, month + 1, last_day)
        except ValueError:
            return date(year, month + 1, 1)
if __name__ == '__main__':
    print(next_month_date(2023, 10))
    print(next_month_date(2023, 12))