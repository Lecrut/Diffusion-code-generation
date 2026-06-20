from datetime import datetime

def calculate_time_difference(start_dt, end_dt, unit):
    delta = end_dt - start_dt
    total_seconds = int(delta.total_seconds())
    if unit == 'days':
        return total_seconds // 86400
    elif unit == 'hours':
        return total_seconds // 3600
    elif unit == 'minutes':
        return total_seconds // 60
    elif unit == 'seconds':
        return total_seconds
    elif unit == 'human':
        days = total_seconds // 86400
        remainder = total_seconds % 86400
        hours = remainder // 3600
        remainder = remainder % 3600
        minutes = remainder // 60
        seconds = remainder % 60
        return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    else:
        raise ValueError("Unsupported unit")

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 10, 0, 0)
    end = datetime(2023, 1, 2, 12, 30, 45)
    result_days = calculate_time_difference(start, end, 'days')
    result_human = calculate_time_difference(start, end, 'human')
    print(result_days)
    print(result_human)