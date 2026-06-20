from datetime import datetime

SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24

def time_difference(start_date_str, end_date_str, format='seconds'):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d %H:%M:%S')
    duration = end_date - start_date
    if format == 'seconds':
        return duration.total_seconds()
    elif format == 'human_readable':
        days = duration.days
        total_hours = duration.seconds // 3600
        hours = total_hours % HOURS_IN_DAY
        minutes = (duration.seconds // SECONDS_IN_MINUTE) % MINUTES_IN_HOUR
        seconds = duration.seconds % SECONDS_IN_MINUTE
        return f'{days} days, {hours} hours'

if __name__ == '__main__':
    start_date = '2023-10-01 12:00:00'
    end_date = '2023-10-05 18:30:00'
    print(time_difference(start_date, end_date, format='human_readable'))