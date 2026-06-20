from datetime import datetime

def calculate_duration(start_date, end_date, format='seconds'):
    start = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
    duration = end - start
    if format == 'seconds':
        return duration.total_seconds()
    elif format == 'human_readable':
        days = duration.days
        hours = duration.seconds // 3600
        minutes = (duration.seconds // 60) % 60
        seconds = duration.seconds % 60
        return f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds'

if __name__ == '__main__':
    start_date = '2023-10-01 12:00:00'
    end_date = '2023-10-05 14:30:00'
    print(calculate_duration(start_date, end_date))
    print(calculate_duration(start_date, end_date, format='human_readable'))