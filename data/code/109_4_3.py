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
        return (31 if next_month == 12 else 30 if next_month in [1, 3, 5, 7, 8, 10, 12] else 28) - today.day
if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    result = days_remaining(sample_date)
    print(result)