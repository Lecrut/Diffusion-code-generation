import datetime

def is_weekend(date_str):
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return date.weekday() >= 5

if __name__ == '__main__':
    sample_date = '2023-10-07'
    print(is_weekend(sample_date))