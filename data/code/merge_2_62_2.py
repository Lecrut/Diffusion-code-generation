from datetime import date
def add_months(current_date: date, months_to_add: int) -> date:
    year = current_date.year + (current_date.month - 1 + months_to_add) // 12
    month = ((current_date.month - 1 + months_to_add) % 12) + 1
    day = min(current_date.day, calendar_days_in_month(year, month))
    return date(year, month, day)
def calendar_days_in_month(year: int, month: int) -> int:
    if month == 2 and (year % 4 == 0 or year % 100 != 0):
        return 29
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
if __name__ == '__main__':
    start_date = date(2023, 5, 1)
    result_date = add_months(start_date, 7)
    print(result_date)