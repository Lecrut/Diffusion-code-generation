from datetime import datetime

def calculate_time_difference(start_datetime, end_datetime, unit):
    time_difference = end_datetime - start_datetime
    if unit == 'days':
        return time_difference.days
    elif unit == 'hours':
        return int(time_difference.total_seconds() / 3600)
    elif unit == 'minutes':
        return int(time_difference.total_seconds() / 60)
    else:
        raise ValueError("Unsupported unit. Use 'days', 'hours', or 'minutes'.")

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 12, 0, 0)
    end = datetime(2023, 1, 2, 14, 30, 0)
    unit = 'hours'
    result = calculate_time_difference(start, end, unit)
    print(result)