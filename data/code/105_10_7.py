from datetime import datetime, timedelta

def get_next_day(date_str: str) -> datetime:
    current_date = datetime.strptime(date_str, '%Y-%m-%d')
    delta = timedelta(days=1)
    next_date = current_date + delta
    return next_date

if __name__ == '__main__':
    input_date = '2024-02-28'
    computed_date = get_next_day(input_date)
    print(computed_date)