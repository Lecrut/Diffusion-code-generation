from datetime import datetime

def is_weekday(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05']
    for date in sample_dates:
        print(f'{date} is a weekday: {is_weekday(date)}')