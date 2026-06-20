from datetime import datetime, timedelta

def next_weekday(start_date, weekday):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    days_ahead = (weekday - start_date.weekday() + 7) % 7
    return (start_date + timedelta(days=days_ahead)).strftime('%Y-%m-%d')
if __name__ == '__main__':
    print(next_weekday('2023-10-01', 4))