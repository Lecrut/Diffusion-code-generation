from datetime import datetime, timedelta

def calculate_next_day(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    next_day = date_obj + timedelta(days=1)
    return next_day

if __name__ == '__main__':
    sample_date = '2023-11-25'
    result = calculate_next_day(sample_date)
    print(result)