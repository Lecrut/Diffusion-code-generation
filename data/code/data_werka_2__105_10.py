from datetime import datetime, timedelta

def get_next_day(date_str: str) -> datetime:
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    next_day = date_obj + timedelta(days=1)
    return next_day

if __name__ == '__main__':
    sample_date = '2023-10-31'
    result = get_next_day(sample_date)
    print(result)