from datetime import date
import calendar

def subtract_months(target_date, months_to_subtract):
    year = target_date.year
    month = target_date.month
    day = target_date.day
    month -= months_to_subtract
    year += (month - 1) // 12
    month = (month - 1) % 12 + 1
    max_day = calendar.monthrange(year, month)[1]
    day = min(day, max_day)
    return date(year, month, day)

if __name__ == '__main__':
    original_date = date(2023, 10, 15)
    result = subtract_months(original_date, 3)
    print(result)