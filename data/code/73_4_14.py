from datetime import datetime

def calculate_duration(start_date_str, end_date_str, format='seconds'):
    date_format = '%Y-%m-%d %H:%M:%S'
    start_date = datetime.strptime(start_date_str, date_format)
    end_date = datetime.strptime(end_date_str, date_format)
    duration = end_date - start_date
    if format == 'seconds':
        return duration.total_seconds()
    elif format == 'human_readable':
        days = duration.days
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f'{days} days, {hours} hours'

if __name__ == '__main__':
    start_date = '2023-10-01 12:00:00'
    end_date = '2023-10-05 18:30:00'
    print(calculate_duration(start_date, end_date, format='human_readable'))