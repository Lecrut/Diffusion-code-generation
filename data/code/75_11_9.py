from datetime import datetime

def date_difference(date1, date2):
    diff = abs((date1 - date2).days)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_diff = (date1.year - date2.year) * 12 + date1.month - date2.month
    if months_diff < 0:
        months_diff += 12
        diff -= days_in_month[date2.month - 1] if date2.month != 2 else 29 if (date2.year % 4 == 0 and date2.year % 100 != 0) or date2.year % 400 == 0 else 28
    months = min(months_diff, diff // 30)
    days = diff % 30
    return f'{months} months, {days} days'

if __name__ == '__main__':
    date_a = datetime(2022, 10, 5)
    date_b = datetime(2024, 6, 3)
    result1 = date_difference(date_a, date_b)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {result1}")