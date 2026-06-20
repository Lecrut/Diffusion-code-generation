from datetime import datetime, timedelta

def get_next_weekday(start_date_str, target_weekday):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    days_to_add = (target_weekday - start_date.weekday() + 7) % 7
    return (start_date + timedelta(days=days_to_add)).strftime('%Y-%m-%d')
if __name__ == '__main__':
    start_date = '2023-10-01'
    target_weekday = 4
    result = get_next_weekday(start_date, target_weekday)
    print(result)