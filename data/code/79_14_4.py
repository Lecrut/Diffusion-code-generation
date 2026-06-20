from datetime import datetime, timedelta

def first_day_next_month(date):
    return (date.replace(day=28) + timedelta(days=4)).replace(day=1)

if __name__ == '__main__':
    sample_date = datetime(2024, 3, 31)
    print(first_day_next_month(sample_date).strftime('%Y-%m-%d'))