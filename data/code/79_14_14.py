from datetime import datetime, timedelta

def get_first_day_next_month():
    current_date = datetime(2024, 3, 31)
    next_month = current_date.replace(day=1) + timedelta(days=31)
    return next_month.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(get_first_day_next_month())