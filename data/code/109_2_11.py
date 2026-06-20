from datetime import datetime, timedelta

def remaining_time_in_month(start_date_str='2023-04-01', end_date_str='2023-05-01'):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    return end_date - start_date

if __name__ == '__main__':
    remaining_time = remaining_time_in_month()
    print(remaining_time)