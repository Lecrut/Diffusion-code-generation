from datetime import date

def subtract_months(d: date, n: int) -> date:
    total_months = d.year * 12 + d.month - n
    year = total_months // 12
    month = total_months % 12
    if month == 0:
        year -= 1
        month = 12
    day = min(d.day, 29 if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return date(year, month, day)

if __name__ == '__main__':
    original_date = date(2023, 10, 15)
    result = subtract_months(original_date, 3)
    print(result)