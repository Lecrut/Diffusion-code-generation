from datetime import datetime

UNIT_MAP = {
    'seconds': 1,
    'minutes': 60,
    'hours': 3600,
    'days': 86400,
}

TARGET_UNIT = 'minutes'
CONVERSION_FACTOR = UNIT_MAP[TARGET_UNIT]

def calculate_date_difference_in_minutes(date_str_a, date_str_b):
    fmt = '%Y-%m-%d %H:%M:%S'
    dt_a = datetime.strptime(date_str_a, fmt)
    dt_b = datetime.strptime(date_str_b, fmt)
    delta_seconds = (dt_b - dt_a).total_seconds()
    return delta_seconds / CONVERSION_FACTOR

if __name__ == '__main__':
    start_time = '2023-01-01 10:00:00'
    end_time = '2023-01-01 12:30:00'
    diff = calculate_date_difference_in_minutes(start_time, end_time)
    print(diff)