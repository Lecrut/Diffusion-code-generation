from datetime import date
def days_remaining(current_date):
    today = date.today()
    current_month = today.month
    current_year = today.year
    if current_month == today.month:
        return 0
    else:
        next_month = current_month + 1
        next_year = current_year
        if next_month > 12:
            next_month = 1
            next_year += 1
        next_month_date = date(next_year, next_month, 1)
        days_in_current_month = (date(current_year, current_month + 1, 1) - date(current_year, current_month, 1)).days
        days_remaining = (date(current_year, current_month + 1, 1) - today).days
        return days_remaining
if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    result = days_remaining(sample_date)
    print(result)