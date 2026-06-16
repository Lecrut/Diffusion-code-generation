from datetime import date
def days_until_month_end(full_date: date) -> int:
    year = full_date.year
    month = full_date.month
    if month == 12:
        return 0
    next_month = month + 1
    if next_month > 12:
        next_month = 1
        year += 1
    first_day_of_next_month = date(year, next_month, 1)
    days_in_current_month = (date(year, month + 1, 1) - date(year, month, 1)).days
    return (date(year, month + 1, 1) - full_date).days
if __name__ == '__main__':
    date1 = date(2023, 10, 15)
    print(f"Date: {date1}, Days remaining until end of month: {days_until_month_end(date1)}")
    date2 = date(2024, 1, 5)
    print(f"Date: {date2}, Days remaining until end of month: {days_until_month_end(date2)}")
    date3 = date(2025, 12, 31)
    print(f"Date: {date3}, Days remaining until end of month: {days_until_month_end(date3)}")
    date4 = date(2023, 5, 1)
    print(f"Date: {date4}, Days remaining until end of month: {days_until_month_end(date4)}")