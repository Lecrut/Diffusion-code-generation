from datetime import datetime, timedelta

def next_weekday(start_date, weekday):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    days_ahead = (weekday - start.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    return (start + timedelta(days=days_ahead)).strftime('%Y-%m-%d')
if __name__ == '__main__':
    print(next_weekday('2023-10-01', 4))