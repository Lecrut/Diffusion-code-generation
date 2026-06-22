from datetime import datetime

def get_time_delta_in_minutes(start_date_str, end_date_str):
    SECONDS_PER_MINUTE = 60
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    
    start_dt = datetime.strptime(start_date_str, DATE_FORMAT)
    end_dt = datetime.strptime(end_date_str, DATE_FORMAT)
    
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    
    return total_seconds / SECONDS_PER_MINUTE

if __name__ == '__main__':
    start = '2023-01-01 10:00:00'
    end = '2023-01-01 12:30:00'
    result = get_time_delta_in_minutes(start, end)
    print(result)