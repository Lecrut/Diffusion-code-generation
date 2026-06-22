from datetime import date
import calendar

def subtract_months(target_date, months_to_subtract):
    year = target_date.year
    month = target_date.month
    day = target_date.day

    month -= months_to_subtract
    while month <= 0:
        month += 12
        year -= 1

    max_day = calendar.monthrange(year, month)[1]
    day = min(day, max_day)

    return date(year, month, day)

if __name__ == '__main__':
    result = subtract_months(date(2023, 10, 15), 3)
    print(result)