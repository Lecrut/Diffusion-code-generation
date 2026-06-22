from datetime import datetime, timedelta

def next_weekday(start_date_str, target_weekday):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    days_ahead = target_weekday - start_date.weekday()
    if days_ahead < 0:
        days_ahead += 7
    next_date = start_date + timedelta(days=days_ahead)
    return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    result = next_weekday('2023-10-01', 4)
    print(result)