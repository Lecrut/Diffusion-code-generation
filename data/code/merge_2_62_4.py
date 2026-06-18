from datetime import date, timedelta
def add_months(d: date, months: int) -> date:
    year = d.year + (months // 12)
    month = d.month - ((d.month + months - 1) % 12) if months > 0 else d.month + months
    while month <= 0:
        year -= 1
        month += 12
    day = min(d.day, [31, 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28, 
                      31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return date(year, month, day)
if __name__ == '__main__':
    sample_date = date(2024, 2, 29)
    months_to_add = 5
    result = add_months(sample_date, months_to_add)
    print(result.strftime("%Y-%m-%d"))