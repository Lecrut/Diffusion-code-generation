from datetime import date
import calendar

def compute_day_difference(first: date, second: date) -> int:
    if not isinstance(first, date) or not isinstance(second, date):
        raise TypeError("Arguments must be instances of datetime.date")
    ordinal_first = first.toordinal()
    ordinal_second = second.toordinal()
    return ordinal_second - ordinal_first

if __name__ == '__main__':
    start_date = date(2023, 12, 1)
    end_date = date(2023, 12, 25)
    diff = compute_day_difference(start_date, end_date)
    print(diff)