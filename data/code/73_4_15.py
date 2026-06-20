from datetime import datetime

def calculate_duration(date_str1, date_str2, format='seconds'):
    date_format = "%Y-%m-%d %H:%M:%S"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    duration = date2 - date1
    if format == 'seconds':
        return duration.total_seconds()
    elif format == 'human_readable':
        days = duration.days
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60
        seconds = duration.seconds % 60
        return f'{days} days, {hours} hours'

if __name__ == '__main__':
    print(calculate_duration('2023-10-01 12:00:00', '2023-10-02 14:30:00'))
    print(calculate_duration('2023-10-01 12:00:00', '2023-10-02 14:30:00', format='human_readable'))