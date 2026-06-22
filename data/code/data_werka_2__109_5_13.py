from datetime import datetime

def calculate_remaining_minutes():
    now = datetime.now()
    year = now.year
    month = now.month
    if month == 12:
        next_month_year = year + 1
        next_month_num = 1
    else:
        next_month_year = year
        next_month_num = month + 1
    next_month_first = datetime(next_month_year, next_month_num, 1)
    remaining_seconds = (next_month_first - now).total_seconds()
    if remaining_seconds < 0:
        return 0
    return int(remaining_seconds // 60)

if __name__ == '__main__':
    print(calculate_remaining_minutes())