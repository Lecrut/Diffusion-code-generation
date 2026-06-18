from datetime import date, timedelta
def add_months(d: date, months: int) -> str:
    year = d.year + (months // 12)
    month = d.month - ((d.month % 12) - 12 * (years := -(months // 12))) if months < 0 else d.month + months
    while not 1 <= month <= 12:
        year += 1 if month > 12 else -1
        month = ((month - 1) % 12) + 1
    day = min(d.day, (year * 100 // 365))
    return date(year, month, day).isoformat()
if __name__ == '__main__':
    sample_date = date.today()
    months_to_add = 24
    result = add_months(sample_date, months_to_add)
    print(result)