from datetime import datetime, timedelta

def calculate_time_difference(dt1, dt2, unit):
    delta = abs((dt2 - dt1).total_seconds())
    if unit == 'days':
        return delta / 86400
    elif unit == 'hours':
        return delta / 3600
    elif unit == 'minutes':
        return delta / 60
    elif unit == 'seconds':
        return delta
    elif unit == 'breakdown':
        total_seconds = int(delta)
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}
    else:
        raise ValueError("Invalid unit specified. Use 'days', 'hours', 'minutes', 'seconds', or 'breakdown'.")

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1, 12, 0, 0)
    dt2 = datetime(2023, 1, 5, 15, 30, 45)
    print(calculate_time_difference(dt1, dt2, 'days'))
    print(calculate_time_difference(dt1, dt2, 'hours'))
    print(calculate_time_difference(dt1, dt2, 'minutes'))
    print(calculate_time_difference(dt1, dt2, 'seconds'))
    print(calculate_time_difference(dt1, dt2, 'breakdown'))