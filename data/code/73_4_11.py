from datetime import datetime

def calculate_duration(start_date, end_date, format='total_seconds'):
    start = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
    duration = (end - start).total_seconds()
    if format == 'human_readable':
        days = int(duration // 86400)
        hours = int(duration % 86400 // 3600)
        return f'{days} days, {hours} hours'
    else:
        return duration
if __name__ == '__main__':
    start_date = '2023-10-01 12:00:00'
    end_date = '2023-10-05 14:30:00'
    print(calculate_duration(start_date, end_date))
    print(calculate_duration(start_date, end_date, 'human_readable'))