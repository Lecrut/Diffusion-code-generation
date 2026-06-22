from datetime import datetime

def calculate_time_difference(datetime1, datetime2, unit):
    difference = abs((datetime2 - datetime1).total_seconds())
    
    if unit == 'days':
        return difference / (60 * 60 * 24)
    elif unit == 'hours':
        return difference / (60 * 60)
    elif unit == 'minutes':
        return difference / 60
    elif unit == 'seconds':
        return difference
    else:
        raise ValueError("Unsupported unit. Please choose from 'days', 'hours', 'minutes', or 'seconds'.")

if __name__ == '__main__':
    datetime1 = datetime(2023, 1, 1, 12, 0, 0)
    datetime2 = datetime(2023, 1, 2, 14, 30, 0)
    
    unit = 'hours'
    result = calculate_time_difference(datetime1, datetime2, unit)
    print(result)