from datetime import datetime

def get_first_day_next_month():
    sample_date = datetime(2024, 3, 31)
    next_month = sample_date.replace(day=28) + timedelta(days=4)
    return next_month.replace(day=1).strftime('%Y-%m-%d')

if __name__ == '__main__':
    result = get_first_day_next_month()
    print(result)