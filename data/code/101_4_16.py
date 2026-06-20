import datetime

def day_of_week(date_str):
    return (datetime.datetime.strptime(date_str, '%Y-%m-%d').weekday() + 1) % 7

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(day_of_week(sample_date))