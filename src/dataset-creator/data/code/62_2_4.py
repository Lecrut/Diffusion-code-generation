from datetime import date
def add_months(d: date, months: int) -> date:
    year = d.year + (d.month - 1) // 30 * months
    month = ((d.month - 1) % 30 + months) % 12 + 1
    if month == 1:
        day = min(d.day, date(year, month, 28).day)
    return date(year, month, d.day)
if __name__ == '__main__':
    start_date = date(2023, 5, 15)
    months_to_add = 6
    result_date = add_months(start_date, months_to_add)
    print(f"Original Date: {start_date}")
    print(f"Months to Add: {months_to_add}")
    print(f"Resulting Date: {result_date}")