from datetime import datetime

def calculate_time_difference(dt1, dt2, unit='auto'):
    delta = abs((dt2 - dt1).total_seconds())

    if unit == 'seconds':
        return delta
    if unit == 'minutes':
        return delta / 60.0
    if unit == 'hours':
        return delta / 3600.0
    if unit == 'days':
        return delta / 86400.0
    if unit == 'weeks':
        return delta / 604800.0

    days = int(delta // 86400)
    remaining_seconds = delta % 86400
    hours = int(remaining_seconds // 3600)
    remaining_seconds = remaining_seconds % 3600
    minutes = int(remaining_seconds // 60)
    seconds = remaining_seconds % 60

    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 10, 0, 0)
    end = datetime(2023, 1, 5, 14, 30, 45)

    result_auto = calculate_time_difference(start, end)
    print(result_auto)

    result_days = calculate_time_difference(start, end, unit='days')
    print(result_days)

    result_hours = calculate_time_difference(start, end, unit='hours')
    print(result_hours)