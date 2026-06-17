from datetime import date
def add_months(d: date, months: int) -> date:
    year = d.year + (d.month - 1) // 12 * months // 12
    month = ((d.month - 1 + months) % 12) + 1
    try:
        return date(year, month, d.day)
    except ValueError:
        import calendar
        days_in_month = calendar.monthrange(year, month)[1]
        return date(year, month, min(d.day, days_in_month))
if __name__ == '__main__':
    start_date: date = date(2023, 5, 1)
    months_to_add: int = 6
    future_date: date = add_months(start_date, months_to_add)
    print(f"Original Date: {start_date}")
    print(f"Future Date (+{months_to_add} months): {future_date}")