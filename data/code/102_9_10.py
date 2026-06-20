from datetime import datetime

def is_weekday(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_dates = ['2023-10-05', '2023-10-06', '2023-10-07']
    results = {date: is_weekday(date) for date in sample_dates}
    print(results)