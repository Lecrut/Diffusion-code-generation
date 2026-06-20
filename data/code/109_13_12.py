from datetime import datetime, timedelta

def time_left_in_month(start_date_str='2023-04-01', end_date_str='2023-05-01'):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    days_left = (end_date - start_date).days
    return days_left

if __name__ == '__main__':
    print(time_left_in_month())