import datetime

def get_next_month_date(start_date):
    months = {
        1: 31,
        2: 29 if (start_date.year % 4 == 0 and start_date.year % 100 != 0) or start_date.year % 400 == 0 else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    current_month = start_date.month
    next_month = (current_month % 12) + 1 if current_month < 12 else 1
    year = start_date.year + (current_month // 12)
    day = min(start_date.day, months[next_month])
    return datetime.datetime(year, next_month, day)

if __name__ == '__main__':
    start_date = datetime.datetime(2023, 1, 15)
    next_month_date = get_next_month_date(start_date)
    print(next_month_date.strftime('%Y-%m-%d'))