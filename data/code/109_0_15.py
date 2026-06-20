import datetime

def days_in_month(year, month):
    if month == 12:
        return (datetime.date(year + 1, 1, 1) - datetime.date(year, month, 1)).days
    else:
        return (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days

def days_remaining_in_month(current_year, current_month):
    today = datetime.date.today()
    if current_year == today.year and current_month == today.month:
        return days_in_month(today.year, today.month) - today.day
    else:
        return days_in_month(current_year, current_month)

if __name__ == '__main__':
    sample_current_year = 2024
    sample_current_month = 10
    remaining_days = days_remaining_in_month(sample_current_year, sample_current_month)
    print(remaining_days)