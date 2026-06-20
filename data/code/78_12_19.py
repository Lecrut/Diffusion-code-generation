from datetime import date, timedelta

def months_difference(date1, date2):
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError('Both inputs must be date objects.')
    year_diff = date2.year - date1.year
    month_diff = date2.month - date1.month
    if date2.day < date1.day:
        month_diff -= 1
    total_months = year_diff * 12 + month_diff
    return abs(total_months)
if __name__ == '__main__':
    date1 = date(2023, 5, 15)
    date2 = date(2024, 3, 10)
    print(months_difference(date1, date2))