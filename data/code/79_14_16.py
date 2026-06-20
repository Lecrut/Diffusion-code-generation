from datetime import datetime, timedelta

def first_day_of_next_month(date):
    if date.month == 12:
        return (date.replace(year=date.year + 1, month=1) + timedelta(days=1)).replace(day=1)
    else:
        return (date.replace(month=date.month + 1) + timedelta(days=1)).replace(day=1)

if __name__ == '__main__':
    sample_date = datetime(2024, 3, 31)
    print(first_day_of_next_month(sample_date).strftime('%Y-%m-%d'))